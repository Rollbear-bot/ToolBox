# -*- coding: utf-8 -*-
# @Time: 2020/4/3 22:32
# @Author: Rollbear
# @Filename: path.py
# 文件路径工具


def path_converter(path: str, work_path: str, mode="rel"):
    """
    文件路径转换器
    :param path: 路径
    :param mode: 转化模式
    :param work_path: 工作路径
    :return: 转换结果
    模式mode=rel，从绝对路径转化为相对路径
    """
    if mode == "rel":
        cut = path.find(work_path)
        if cut == -1:
            return None  # 传入了错误的路径
        return "." + path[len(work_path):]
    return None  # 未知的处理模式

