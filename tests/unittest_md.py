# 测试用例
import md_parser as mdp
import unittest

from service.converter import *
from service.searcher import *
from entity.document import Document


def load_test_file_lines():
    return open('notes.md', 'r', encoding='utf8').readlines()


def load_test_file_path():
    return 'notes.md'


class TestScanner(unittest.TestCase):

    def test_scanner_and_printer(self):
        origin = load_test_file_lines()
        lt = printer(scanner(load_test_file_lines()))

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


class TestMigrate(unittest.TestCase):
    """迁移测试"""
    def test_pict_migrate(self):
        """测试图片源迁移"""
        doc = Document(load_test_file_path())
        new_path = "./pict"
        doc.pict_migrate(new_path)
        for pict in doc.pictures:
            self.assertEqual(pict.src, new_path)
            self.assertTrue(new_path in doc.raw_lines[pict.location])


class TestDocObject(unittest.TestCase):
    """测试文档对象"""
    def test_deep_copy(self):
        """测试Document对象的深复制"""
        doc1 = Document(load_test_file_path())
        doc2 = doc1.copy()
        doc2.raw_lines[0] = "# "
        doc2.root_topic.text.append(" ")
        self.assertNotEqual(doc1.raw_lines[0], "# ")
        self.assertEqual(len(doc1.root_topic.text), 0)


if __name__ == '__main__':
    unittest.main()
