from main import parser

# from pytest import mocker
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
