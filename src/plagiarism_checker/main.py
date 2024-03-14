import argparse
import checker, pre
import time
from io import TextIOWrapper

parser = argparse.ArgumentParser(description="simple python plagiarism checker")

parser.add_argument(
    "origin_file", type=argparse.FileType("r", encoding="utf-8"), help="原文件路径"
)
parser.add_argument(
    "check_file", type=argparse.FileType("r", encoding="utf-8"), help="检查文件路径"
)
parser.add_argument(
    "output_file", type=argparse.FileType("w", encoding="utf-8"), help="输出文件路径"
)
parser.add_argument(
    "--debug", action="store_true", help="开启性能分析"
)



def output_result(output_file: TextIOWrapper, result: float):
    """输出结果到文件和控制台"""
    output = round(result, 2)
    print(output)
    try:
        output_file.write(str(output))
    except Exception as e:
        print(e)
        print("输出文件失败")


def main():
    try:
        args = parser.parse_args()
        # print(args)
    except Exception as e:
        # 当遇到错误会抛出异常，argparse 错误信息写的很详细，不再做处理
        print("error")
        print(e)

    if args.debug:
        from pyinstrument import Profiler
        p = Profiler()
        p.start()

    origin = args.origin_file.read()
    check = args.check_file.read()
    output = args.output_file
    texts = [origin, check]
    # 预处理
    texts = [pre.data_preprocessing(text) for text in texts]
    # 计算 tf-idf
    tf_idf = checker.cal_tf_idf(texts)
    similarity_matrix = checker.cosine_similarity(tf_idf)
    # 输出结果
    output_result(output, similarity_matrix[0][1])

    if args.debug:
        p.stop()
        p.output_html()
        # p.output_text()
        # p.open_in_browser()

if __name__ == "__main__":
    main()
