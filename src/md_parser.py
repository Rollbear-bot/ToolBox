# -*- coding: utf-8 -*-
# @Time: 2020/3/13 7：28
# @Author: Rollbear
# @Filename: md_parser.py
# markdown分析器

import tkinter
from util import path
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

    doc = document.Document(file_path)
    doc.show_all_topic()

    # 以下为图片源迁移功能
    print("选择新的图片源目录...")
    new_dir = filedialog.askdirectory()

    new_doc_name = input("新的Markdown文档名（不需要后缀）：")
    print("保存文档到...")
    work_dir = filedialog.askdirectory()
    doc_path = work_dir + "/" + new_doc_name + ".md"

    # 使用相对路径来构造图片标签
    doc.pict_migrate(path.path_converter(new_dir, work_dir, mode="rel"))
    # 保存Markdown文档到指定的路径
    doc.save(doc_path)


if __name__ == '__main__':
    main()
