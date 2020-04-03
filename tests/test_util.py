# -*- coding: utf-8 -*-
# @Time: 2020/4/3 22:39
# @Author: Rollbear
# @Filename: test_util.py

import unittest
from util.path import *


class TestPath(unittest.TestCase):
    """路径工具测试"""
    def test_path_converter(self):
        """测试路径转换工具"""
        abs_path = "c:/user/document/test/pict.png"
        work_path = "c:/user/document"
        expected = "./test/pict.png"
        res = path_converter(abs_path, work_path, mode="rel")
        self.assertEqual(res, expected)
