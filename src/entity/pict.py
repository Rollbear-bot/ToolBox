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
        self.src_dir, self.src_pict_name, self.alt, self.style \
            = Pict.pict_tag_parser(raw_tag)

    def migrate(self, new_dir: str):
        """将当前图片的源迁移到另一个目录"""
        self.src_dir = new_dir
        # 构造新的图片标签
        self.raw_tag = "<img src=\"" \
                       + self.src_dir + "/" + self.src_pict_name \
                       + "\" alt=\"" + self.alt
        if self.style == "":
            self.raw_tag += "\" />"
        else:
            self.raw_tag += "\" style=\"" + self.style + "\" />"

    @staticmethod
    def pict_tag_parser(raw_tag: str):
        """
        图片标签解析器
        :param raw_tag: 原始图片标签
        :return: 四元组（图片源目录，图片源文件名，图片注释，图片缩放数值）
        """
        clip = raw_tag.split('src=\"')
        clip = clip[1].split('\" alt=\"')
        src_dir = clip[0]
        src_pict_name = src_dir.rsplit("/")[1]
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
        return src_dir, src_pict_name, alt, style

