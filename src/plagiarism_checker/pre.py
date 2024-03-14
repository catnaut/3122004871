import jieba
import jionlp


def data_cleaning(str: str) -> str:
    # 调用 jionlp 库实现文本清洗
    return jionlp.clean_text(str)


def data_cut(str: str) -> iter:
    # 调用 jieba 库实现文本分词
    return jieba.cut(str)


def data_preprocessing(str: str) -> list:
    '''文本预处理'''
    return data_cut(data_cleaning(str))
