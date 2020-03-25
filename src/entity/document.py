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
            # 打开文件
            lines = open(file_path, 'r', encoding='utf8').readlines()
            if not lines[0].startswith("# "):
                raise UnexpectedFile  # 文档的第一行必须是顶级标题，否则无法创建根话题
            self.root_topic = scanner(lines)
            self.pictures = pict_searcher(lines)
            self.doc_path = file_path

    def __str__(self):
        return self.root_topic.title

    def show_all_topic(self):
        """打印当前文档对象的所有标题"""
        _show_topic_list(self.root_topic)

    def copy(self):
        """深拷贝一个Document对象"""
        clone = Document()
        clone.pictures = self.pictures.copy()
        # 拷贝对象应该重新生成话题树
        clone.root_topic = scanner(self.raw_lines())
        clone.doc_path = None
        return clone

    def pict_migrate(self, new_path: str):
        """将本文档中所有图片的源迁移到新目录"""
        lines = self.raw_lines()
        for pict in self.pictures:
            pict.migrate(new_path)
            line = lines[pict.location]
            # todo::可能会识别到其他标签尾，也不能正常识别同一行的第二张图片
            img_start = line.find("<img")
            img_end = line.find("/>")
            # 将新的图像路径插入文档行
            lines[pict.location] \
                = line[:img_start] + pict.raw_tag() + line[img_end+2:]
            # 用更改后的文档行重新生成话题树
            self.root_topic = scanner(lines)

    def save(self, path: str):
        """
        将对象以文本文件方式保存
        :param path: 文件保存路径
        """
        file = open(path, 'w', encoding='utf8')
        file.writelines(self.raw_lines())
        file.close()

    def raw_lines(self):
        """从解析树生成Markdown文本行"""
        return _printer_recursion(self.root_topic, [])


def _printer_recursion(cur: Topic, result: list):
    """对printer的递归实现
    （对结点前序遍历的递归实现）"""
    if not isinstance(cur, Topic):
        return result

    result.append(cur.raw_title)  # 加载标题
    for line in cur.text:
        result.append(line)  # 加载正文
    if len(cur.sub_topic) == 0:  # 递归出口
        return result

    for topic in cur.sub_topic:
        result = _printer_recursion(topic, result)
    return result  # 遍历完成
