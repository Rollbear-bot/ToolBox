# 测试用例
import md_parser as mdp
import unittest

from service.converter import *
from service.searcher import *


def load_test_file_lines():
    return open('notes.md', 'r', encoding='utf8').readlines()


class TestScanner(unittest.TestCase):

    def test_scanner_and_printer(self):
        origin = load_test_file_lines()
        lt = printer(scanner(open('notes.md', 'r', encoding='utf8')))

        # 从解析树获取的markdown文本应当和解析前一致
        self.assertListEqual(lt, origin)


class TestSearcher(unittest.TestCase):
    """元素搜索测试"""
    def test_pict_search(self):
        """测试图片tag的定位"""
        lines = load_test_file_lines()
        result = pict_searcher(lines)
        self.assertEqual(result[0].style, "zoom: 80%;")
        self.assertEqual(result[0].src, '其他笔记.assets/web服务器和web框架.png')
        self.assertEqual(result[1].style, "zoom:67%;")


if __name__ == '__main__':
    unittest.main()
