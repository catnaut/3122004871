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
