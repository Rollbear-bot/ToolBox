# -*- coding: utf-8 -*-
# @Time: 2020/3/24 18:14
# @Author: Rollbear
# @Filename: document.py

from entity.pict import Pict
from entity.topic import Topic
from service.converter import *
from service.searcher import *


def _show_topic_list(cur_topic: Topic):
    """打印当前标题以及它的所有下级标题
    用缩进来表现标题之间的层次关系
    树的递归前序遍历"""
    if len(cur_topic.sub_topic) == 0:
        # 递归出口
        print('\t' * (cur_topic.level - 1) + str(cur_topic))
        return None
    print('\t' * (cur_topic.level - 1) + str(cur_topic))
    # 对子结点递归
    for t in cur_topic.sub_topic:
        _show_topic_list(t)


class UnexpectedFile(Exception):
    """传入了非Markdown文档"""
    def __str__(self):
        return "传入了非Markdown文档"


class Document:
    """Markdown文档对象"""
    def __init__(self, md_file: open):
        self.raw_lines = md_file.readlines()
        if not self.raw_lines[0].startswith("# "):
            raise UnexpectedFile
        self.root_topic = scanner(self.raw_lines)
        self.pictures = pict_searcher(self.raw_lines)

    def __str__(self):
        return self.root_topic.title

    def show_all_topic(self):
        """打印当前文档对象的所有标题"""
        _show_topic_list(self.root_topic)
