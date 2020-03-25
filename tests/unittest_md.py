# 测试用例
import md_parser as mdp
import unittest

from service.converter import *
from service.searcher import *
from entity.document import Document


def load_test_file_path():
    return 'notes.md'


class TestMigrate(unittest.TestCase):
    """迁移测试"""
    def test_pict_migrate(self):
        """测试图片源迁移"""
        doc = Document(load_test_file_path())
        new_path = "./pict"
        doc.pict_migrate(new_path)
        raw_lines = doc.raw_lines()
        for pict in doc.pictures:
            self.assertEqual(pict.src_dir, new_path)
            self.assertTrue(new_path in raw_lines[pict.location])

    def test_pict_migrate_case_2(self):
        doc1 = Document(load_test_file_path())
        doc1.pict_migrate("./pict")
        doc1.save("./t.md")
        doc2 = Document("./t.md")
        for pict in doc2.pictures:
            self.assertEqual(pict.src_dir, "./pict")


class TestDocObject(unittest.TestCase):
    """测试文档对象"""
    def test_deep_copy(self):
        """测试Document对象的深复制"""
        doc1 = Document(load_test_file_path())
        doc2 = doc1.copy()
        doc2.root_topic.text.append(" ")
        self.assertEqual(len(doc1.root_topic.text), 0)


if __name__ == '__main__':
    unittest.main()
