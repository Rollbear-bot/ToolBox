# -*- coding: utf-8 -*-
# @Time: 2020/3/24 16:53
# @Author: Rollbear
# @Filename: pict.py
# Markdown图片对象


class Pict:
    """图片"""
    def __init__(self, raw_tag: str, location: int):
        """构造方法：从一个图片tag构造图片对象"""
        self.raw_tag = raw_tag  # 原始Markdown图片标签
        self.location = location
        self.src, self.alt, self.style = Pict.pict_tag_parser(raw_tag)

    @staticmethod
    def pict_tag_parser(raw_tag: str):
        """图片标签解析器"""
        clip = raw_tag.split('src=\"')
        clip = clip[1].split('\" alt=\"')
        src = clip[0]
        clip = clip[1].split('\" style=\"')
        alt = clip[0]
        clip = clip[1].split('\" /')
        style = clip[0]
        return src, alt, style

