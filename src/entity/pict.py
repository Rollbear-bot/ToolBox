# -*- coding: utf-8 -*-
# @Time: 2020/3/24 16:53
# @Author: Rollbear
# @Filename: pict.py
# Markdown图片对象


class Pict:
    """图片"""
    def __init__(self, raw_tag: str, location: int):
        """构造方法：从一个图片tag构造图片对象"""
        lt = raw_tag.split(" ")  # 使用空格划分标签内的内容
        self.raw_tag = raw_tag  # 原始Markdown图片标签
        self.src = lt[1][5:-1]
        self.alt = lt[2][5:-1]
        self.style = lt[3][7:-1]
        self.location = location

