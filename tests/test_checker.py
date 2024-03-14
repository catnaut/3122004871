import checker

class TestChecker:
    def test_cal_cosine_similarity(self):
        # 测试余弦相似度计算，返回值为一个 2 x 2 的矩阵
        r = checker.cal_cosine_similarity([[1, 2], [3, 4]])
        assert r.shape == (2, 2)