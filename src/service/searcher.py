# -*- coding: utf-8 -*-
# @Time: 2020/3/24 16:48
# @Author: Rollbear
# @Filename: searcher.py

from entity.pict import Pict


class UnknownImgFormat(Exception):
    """未知的图片格式"""
    def __str__(self):
        return "未知的图片格式"


def pict_searcher(lines: iter):
    """
    定位Markdown文档中的图片
    :param lines: Markdown文本（行作为元素的列表）
    :return: Pict对象的列表
    """
    result = []
    for index in range(len(lines)):
        cur_pict = None
        # 通过img标签的方式搜索
        location = lines[index].find("<img ")
        if location != -1:
            raw_tag \
                = lines[index][location:lines[index].find("/>")+2]
            cur_pict = Pict(raw_tag, index)
            result.append(cur_pict)
        # 通过"![]"的格式搜索
        else:
            start = lines[index].find("![")
            if start == -1:
                continue
            end = lines[index].find(".jpg)")
            if end == -1:
                end = lines[index].find(".png)")
                if end == -1:
                    raise UnknownImgFormat
            cur_pict = Pict(lines[index][start:end+5], index, classic=True)
            result.append(cur_pict)

    return result
