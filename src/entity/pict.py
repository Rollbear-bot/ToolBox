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

    def migrate(self, new_path: str):
        """将当前图片的源迁移到另一个目录"""
        self.src = new_path
        self.raw_tag = "<img src=\"" + self.src + "\" alt=\"" + self.alt
        if self.style == "":
            self.raw_tag += "\" />"
        else:
            self.raw_tag += "\" style=\"" + self.style + "\" />"

    @staticmethod
    def pict_tag_parser(raw_tag: str):
        """图片标签解析器"""
        clip = raw_tag.split('src=\"')
        clip = clip[1].split('\" alt=\"')
        src = clip[0]
        clip = clip[1].split('\" style=\"')
        alt = clip[0]
        tmp = alt.rfind('/>')
        if tmp != -1:
            alt = alt[:tmp-3]
        # style在图片标签中是可缺省的
        style = ""
        if len(clip) > 1:
            clip = clip[1].split('\" /')
            style = clip[0]
        return src, alt, style

