# -*- coding: utf-8 -*-
# @Time: 2020/3/13 15:28
# @Author: Rollbear
# @Filename: topic.py


class Topic(object):
    """主题类
    树形结构中的结点"""
    def __init__(self, raw_title: str):
        self.raw_title = raw_title  # 标题（带井号和空格的md格式标题）
        self.title = raw_title[raw_title.find(' ')+1:-1]  # 提取标题文本
        self.sub_topic = []  # 该标题下的子标题
        self.parent_topic = None  # 父级标题
        self.text = []  # 该标题下的正文（非其他子标题下）
        # 标题等级，顶级标题level=1
        self.level = raw_title.split(' ')[0].count('#')

    def __str__(self):
        return self.title + f"（{self.level}级标题）"
