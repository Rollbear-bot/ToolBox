# -*- coding: utf-8 -*-
# @Time: 2020/3/24 18:14
# @Author: Rollbear
# @Filename: document.py

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
    def __init__(self, file_path=None):
        if file_path:
            if not file_path.endswith(".md"):
                raise UnexpectedFile  # 如果传入的不是md文件则抛出异常

            md_file = open(file_path, 'r', encoding='utf8')  # 打开文件
            self.raw_lines = md_file.readlines()
            if not self.raw_lines[0].startswith("# "):
                raise UnexpectedFile  # 文档的第一行必须是顶级标题，否则无法创建根话题
            self.root_topic = scanner(self.raw_lines)
            self.pictures = pict_searcher(self.raw_lines)
            self.doc_path = file_path

    def __str__(self):
        return self.root_topic.title

    def show_all_topic(self):
        """打印当前文档对象的所有标题"""
        _show_topic_list(self.root_topic)

    def copy(self):
        """深拷贝一个Document对象"""
        clone = Document()
        clone.raw_lines = self.raw_lines.copy()
        clone.pictures = self.pictures.copy()
        # 拷贝对象应该重新生成话题树
        clone.root_topic = scanner(self.raw_lines)
        clone.doc_path = None
        return clone

    def pict_migrate(self, new_path: str):
        """将本文档中所有图片的源迁移到新目录"""
        for pict in self.pictures:
            pict.migrate(new_path)
            line = self.raw_lines[pict.location]
            # todo::可能会识别到其他标签尾，也不能正常识别同一行的第二张图片
            img_start = line.find("<img")
            img_end = line.find("/>")
            # 将新的图像路径插入文档行
            self.raw_lines[pict.location] \
                = line[:img_start] + pict.raw_tag + line[img_end+2:]
            # 用更改后的文档行重新生成话题树
            self.root_topic = scanner(self.raw_lines)
