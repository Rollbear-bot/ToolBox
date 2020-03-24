# -*- coding: utf-8 -*-
# @Time: 2020/3/13 7：28
# @Author: Rollbear
# @Filename: md_parser.py
# markdown分析器

import tkinter
from tkinter import filedialog

from entity import document


def main():
    root = tkinter.Tk()
    root.withdraw()

    # 打开一个md文件
    file_path = filedialog.askopenfilename()
    while not str(file_path).endswith('.md'):
        print('你打开的不是markdown文件，请重新选择')
        file_path = filedialog.askopenfilename()

    md_the_file = open(file_path, 'r', encoding='utf8')  # 以只读方式打开
    doc = document.Document(md_the_file)
    doc.show_all_topic()


if __name__ == '__main__':
    main()
