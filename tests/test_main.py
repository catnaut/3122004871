from main import parser

# from pytest import mocker
import sys
from io import TextIOWrapper


class TestMain:
    TESTS_TXT_DIR = "./tests/tests-txt/"

    def test_pytest(self):
        assert 1 == 1

    def test_argparse(self, mocker):
        # tests_txt_dit = "./tests/tests-txt/"
        test_args = [
            ".\\main.py",
            self.TESTS_TXT_DIR + "orig.txt",
            self.TESTS_TXT_DIR + "orig_0.8_add.txt",
            self.TESTS_TXT_DIR + "output.txt",
        ]
        mocker.patch.object(sys, "argv", test_args)
        args = parser.parse_args()
        assert isinstance(args.origin_file, TextIOWrapper)
        assert isinstance(args.check_file, TextIOWrapper)
        assert isinstance(args.output_file, TextIOWrapper)