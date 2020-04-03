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
                = Pict.pict_tag_parser(tag, classic_mode=True)
        else:
            self.src_dir, self.src_pict_name, self.alt, self.style \
                = Pict.pict_tag_parser(tag)

    def raw_tag(self):
        """生成原始图片标签（html风格）"""
        tag = "<img src=\"" \
            + self.src_dir + "/" + self.src_pict_name \
            + "\" alt=\"" + self.alt
        if self.style is None or self.style == "":
            tag += "\" />"
        else:
            tag += "\" style=\"" + self.style + "\" />"
        return tag

    def migrate(self, new_dir: str):
        """将当前图片的源迁移到另一个目录"""
        self.src_dir = new_dir

    @staticmethod
    def pict_tag_parser(raw_tag: str, classic_mode=False):
        """
        图片标签解析器
        经典风格图片标签：![alt_str](image_path)
        html风格图片标签：<img src=... alt=... style=... />
        :param raw_tag: 原始图片标签
        :param classic_mode: 标记是否使用经典风格
        :return: 四元组（图片源目录，图片源文件名，图片注释，图片缩放数值）
        """
        if classic_mode:
            # 使用经典标记风格解析
            clip = raw_tag.split("](")
            alt = clip[0][2:]

            src_clip = clip[1][:-1]
            src_dir, src_pict_name = Pict.path_parser(src_clip)

            style = ""
            return src_dir, src_pict_name, alt, style

        else:
            # 使用html风格标记解析
            clip = raw_tag.split('src=\"')
            clip = clip[1].split('\" alt=\"')

            src_dir, src_pict_name = Pict.path_parser(clip[0])

            clip = clip[1].split('\" style=\"')
            alt = clip[0]
            tmp = alt.rfind('/>')
            if tmp != -1:
                alt = alt[:tmp-3]
            # style在图片标签中是可缺省的
            style = ""
            if len(clip) > 1:
                clip = clip[1].split('\" />')
                style = clip[0]
            return src_dir, src_pict_name, alt, style

    @staticmethod
    def path_parser(img_path: str):
        """从图片源路径中解析出目录路径和文件名"""
        cut = "/"
        if "\\" in img_path:
            cut = "\\"
        cut_index = img_path.rfind(cut)
        src_dir = img_path[:cut_index]
        src_pict_name = img_path[cut_index + 1:]
        return src_dir, src_pict_name
