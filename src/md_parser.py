# -*- coding: utf-8 -*-
# @Time: 2020/3/13 7：28
# @Author: Rollbear
# @Filename: md_parser.py
# markdown分析器

import tkinter
from tkinter import filedialog

from service.converter import scanner, printer
from entity import md_topic


def topic_list(headline: md_topic):
    """打印当前标题以及它的所有下级标题
    用缩进来表现标题之间的层次关系
    树的递归前序遍历"""
    if len(headline.sub_topic) == 0:
        # 递归出口
        print('\t'*(headline.level-1) + str(headline))
        return None
    print('\t'*(headline.level-1) + str(headline))
    # 对子结点递归
    for topic in headline.sub_topic:
        topic_list(topic)


def main():
    root = tkinter.Tk()
    root.withdraw()

    # 打开一个md文件
    file_path = filedialog.askopenfilename()
    while not str(file_path).endswith('.md'):
        print('你打开的不是markdown文件，请重新选择')
        file_path = filedialog.askopenfilename()

    md_the_file = open(file_path, 'r', encoding='utf8')  # 以只读方式打开
    result = scanner(md_file=md_the_file)
    lt = printer(result)
    for line in lt:
        print(line, end='')


if __name__ == '__main__':
    main()
