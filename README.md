# Plagiarism checker

由 Python 实现的简易查重软件

## PSP

| **PSP2.1**                              | **Personal Software Process Stages**    | **预估耗时（分钟）** | **实际耗时（分钟）** |
|--|--|--|--|
| Planning                                | 计划                                    |                      25|                22      |
| · Estimate                              | · 估计这个任务需要多少时间              |                      5|               7       |
| Development                             | 开发                                    |                      480|                460      |
| · Analysis                              | · 需求分析 (包括学习新技术)             |                      120|            110          |
| · Design Spec                           | · 生成设计文档                          |                      30|               10       |
| · Design Review                         | · 设计复审                              |                      30|                 10    |
| · Coding Standard                       | · 代码规范 (为目前的开发制定合适的规范) |                      30|                 5     |
| · Design                                | · 具体设计                              |                      60|                100      |
| · Coding                                | · 具体编码                              |                      120|                200      |
| · Code Review                           | · 代码复审                              |60|                20      |
| · Test                                  | · 测试（自我测试，修改代码，提交修改）  |                      30|                    5 |
| Reporting                               | 报告                                    |                      120|                 70|
| · Test Repor                            | · 测试报告                              |                      30|                  10    |
| · Size Measurement                      | · 计算工作量                            |                      30|                 10     |
| · Postmortem & Process Improvement Plan | · 事后总结, 并提出过程改进计划          |                      30|               60       |
|                                         | ·  合计                                 |                      625|              552        |



## 设计

### 目标
由 Python 实现的简易查重软件

### 背景
作业 [个人项目 - 作业 - 软件工程2024 - 班级博客 - 博客园 (cnblogs.com)](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineering2024/homework/13136)

### 总体设计

命令行输入
文件读取
数据清洗
文本表示
*优化*
相似度计算
输出结果
```ascii
命令行输入 --> 文件读取 --> 数据清洗 --> 文本表示 --> 相似度计算 --> 输出结果
```
### 详细设计

#### 项目管理

使用 PDM

#### 单元测试

pytest

#### 交互 interface

使用 Python 标准库 [argparse](https://docs.python.org/3/library/argparse.html) 库
此库对文件状态，命令行参数位置进行了错误检测，经过测试有完善的报错机制
#### 数据清理

使用 [dongrixinyu/JioNLP: 中文 NLP 预处理、解析工具包，准确、高效、易用 A Chinese NLP Preprocessing & Parsing Package www.jionlp.com (github.com)](https://github.com/dongrixinyu/JioNLP) 项目内的 `clean_txt` 方法
id:: 65f279e0-8341-4383-84f1-e6e748e5c512
该方法实现了对重复符号，异常字符的处理

#### 文本表示

使用 [fxsjy/jieba: 结巴中文分词 (github.com)](https://github.com/fxsjy/jieba)
该库使用广泛，在较短的处理时间内仍然有较好的分词效果

#### 相似度计算

由于要求在短时间给出文本相似度，所以选择传统文本特征算法，基于 sklearn 库
使用  [sklearn.feature_extraction.text.TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.fit) 实现 TF-idf 逆文本出现频率算法
使用 [sklearn.metrics.pairwise.cosine_similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) 实现 余弦相似度
#### 输出结果

输出到控制台和 `output.txt` 文件

## 报告

### 单元测试
测试覆盖率
```shell
 pdm test --cov=src
================================================= test session starts =================================================
platform win32 -- Python 3.12.0, pytest-8.1.1, pluggy-1.4.0
rootdir: O:\Code\python\pc\plagiarism-checker
configfile: pyproject.toml
plugins: cov-4.1.0, mock-3.12.0
collected 6 items

tests\test_checker.py .                                                                                          [ 16%]
tests\test_main.py ..                                                                                            [ 50%]
tests\test_pre.py ...                                                                                            [100%]

---------- coverage: platform win32, python 3.12.0-final-0 -----------
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
src\plagiarism_checker\__init__.py       0      0   100%
src\plagiarism_checker\checker.py        9      3    67%
src\plagiarism_checker\main.py          32     21    34%
src\plagiarism_checker\pre.py            8      0   100%
--------------------------------------------------------
TOTAL                                   49     24    51%


================================================= 6 passed in 25.26s ==================================================
```
```python
###  test_main.py ###
from main import parser
import sys
from io import TextIOWrapper


class TestMain:
    # 测试文件路径
    TESTS_TXT_DIR = "./tests/tests-txt/"

    # 测试 pytest
    def test_pytest(self):
        assert 1 == 1

    # 测试 argparse 是否可以读取文件
    def test_argparse(self, mocker):
        test_args = [
            ".\\main.py",
            self.TESTS_TXT_DIR + "orig.txt",
            self.TESTS_TXT_DIR + "orig_0.8_add.txt",
            self.TESTS_TXT_DIR + "output.txt",
        ]
        # 用 mocker.patch.object 替换 sys.argv
        mocker.patch.object(sys, "argv", test_args)
        args = parser.parse_args()

        # 测试是否可以读取到文件对象
        assert isinstance(args.origin_file, TextIOWrapper)
        assert isinstance(args.check_file, TextIOWrapper)
        assert isinstance(args.output_file, TextIOWrapper)
### test_pre.py ###
import pre


class TestPre:
    def test_cleaning(self):
        # 调用 jionlp 库实现文本清洗，返回值不为即可不产生报错
        r = pre.data_cleaning("你好")
        assert r != None

    def test_cut(self):
        # 调用 jieba 库实现文本分词，返回值不为即可不产生报错
        r = pre.data_cut("你好")
        assert r != None

    def test_preprocessing(self):
        # 测试文本预处理，返回值不为即可不产生报错
        r = pre.data_preprocessing("你好")
        assert r != None

        
        
### test_checker.py ###
import checker

class TestChecker:
    def test_cal_cosine_similarity(self):
        # 测试余弦相似度计算，返回值为一个 2 x 2 的矩阵
        r = checker.cal_cosine_similarity([[1, 2], [3, 4]])
        assert r.shape == (2, 2)
```
### 异常处理
#### `argprase` 报错
```python
try:
    args = parser.parse_args()
    # print(args)
except Exception as e:
    # 当遇到错误会抛出异常，argparse 错误信息写的很详细，不再做处理
    print("error")
    print(e)
```
此库对文件状态，命令行参数位置进行了错误检测，经过测试有完善的报错机制，直接输出报错信息
#### 输出文件报错
```python
def output_result(output_file: TextIOWrapper, result: float):
    """输出结果到文件和控制台"""
    output = round(result, 2)
    print(output)
    try:
        output_file.write(str(output))
    except Exception as e:
        print(e)
        print("输出文件失败")
```
### 性能分析
![image](https://github.com/catnaut/3122004871/assets/127472258/f5857f3e-b54e-4cf4-8c9f-51f2f5a03610)
使用 [pyinstrument](https://pyinstrument.readthedocs.io/en/latest/home.html) 对性能进行分析



