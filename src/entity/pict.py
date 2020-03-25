# -*- coding: utf-8 -*-
# @Time: 2020/3/24 16:53
# @Author: Rollbear
# @Filename: pict.py
# Markdown图片对象


class Pict:
    """图片"""
    def __init__(self, tag: str, location: int, classic=False):
        """构造方法：从一个图片tag构造图片对象"""
        self.location = location
        if classic:
            self.src_dir, self.src_pict_name, self.alt, self.style \
                = Pict.pict_tag_parser_classic(tag)
        else:
            self.src_dir, self.src_pict_name, self.alt, self.style \
                = Pict.pict_tag_parser(tag)

    def raw_tag(self):
        """生成原始图片标签（html风格）"""
        tag = "<img src=\"" \
            + self.src_dir + "/" + self.src_pict_name \
            + "\" alt=\"" + self.alt
        if self.style == "":
            tag += "\" />"
        else:
            tag += "\" style=\"" + self.style + "\" />"
        return tag

    def migrate(self, new_dir: str):
        """将当前图片的源迁移到另一个目录"""
        self.src_dir = new_dir
        # 构造新的图片标签
        '''
        self.raw_tag = "<img src=\"" \
                       + self.src_dir + "/" + self.src_pict_name \
                       + "\" alt=\"" + self.alt
        if self.style == "":
            self.raw_tag += "\" />"
        else:
            self.raw_tag += "\" style=\"" + self.style + "\" />"
        '''

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

    @staticmethod
    def pict_tag_parser_classic(tag: str):
        """
        经典标签解析器
        同时将经典标签转化为html风格
        经典风格图片标签：![alt_str](image_path)
        :param tag: 经典标签
        :return: 四元组（图片源目录，图片源文件名，图片注释，图片缩放数值）
        """
        clip = tag.split("](")
        alt = clip[0][2:]
        src_clip = clip[1][:-1].rsplit("/")
        src_dir = src_clip[0]
        src_pict_name = src_clip[1]
        style = ""
        return src_dir, src_pict_name, alt, style
