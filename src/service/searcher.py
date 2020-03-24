# -*- coding: utf-8 -*-
# @Time: 2020/3/24 16:48
# @Author: Rollbear
# @Filename: searcher.py

from entity.pict import Pict


def pict_searcher(lines: iter):
    """
    定位Markdown文档中的图片
    :param lines: Markdown文本（行作为元素的列表）
    :return: Pict对象的列表
    """
    result = []
    for index in range(len(lines)):
        cur_pict = None
        location = lines[index].find("<img ")
        if location != -1:
            raw_tag \
                = lines[index][location:lines[index].find("/>")+2]
            cur_pict = Pict(raw_tag, index)
            result.append(cur_pict)
    return result
