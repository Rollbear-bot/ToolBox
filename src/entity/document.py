# -*- coding: utf-8 -*-
# @Time: 2020/3/24 18:14
# @Author: Rollbear
# @Filename: document.py

from entity.pict import Pict
from entity.topic import Topic
from service.converter import *
from service.searcher import *


class Document:
    """Markdown文档对象"""
    def __init__(self, md_file: open):
        self.raw_lines = md_file.readlines()
        self.root_topic = scanner(self.raw_lines)
        self.pictures = pict_searcher(self.raw_lines)

    def __str__(self):
        return self.root_topic.title
