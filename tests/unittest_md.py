# 测试用例
import md_parser as mdp
import unittest

from entity.md_topic import Topic
from service.converter import scanner, printer


def load_test_file():
    return open('notes.md', 'r', encoding='utf8')


class TestScanner(unittest.TestCase):

    def test_scanner_and_printer(self):
        file = load_test_file()
        origin = file.readlines()
        file.close()
        lt = printer(scanner(load_test_file()))

        # 从解析树获取的markdown文本应当和解析前一致
        self.assertListEqual(lt, origin)
        file.close()


if __name__ == '__main__':
    unittest.main()
