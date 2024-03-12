import argparse

parser = argparse.ArgumentParser(description="simple python plagiarism checker")

parser.add_argument('origin_file', type=argparse.FileType('r'), help='原文件路径')
parser.add_argument('check_file',type=argparse.FileType('r'),help='检查文件路径')
parser.add_argument('output_file', type=argparse.FileType('w'), help='输出文件路径')


if __name__ == "__main__":
    try:
        args = parser.parse_args()
        print(args)
    except Exception as e:
        print(e)