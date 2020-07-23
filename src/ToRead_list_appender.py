# -*- coding: utf-8 -*-
# @Time: 2020/7/23 18:38
# @Author: Rollbear
# @Filename: ToRead_list_appender.py
# 往一个markdown文件中追加一个阅读计划

import os
import tkinter
from tkinter import filedialog
from tkinter import messagebox


def main():
    root = tkinter.Tk()
    root.withdraw()

    # 打开一个md文件
    md_path = filedialog.askopenfilename()
    while not str(md_path).endswith('.md'):
        print('你打开的不是markdown文件，请重新选择')
        md_path = filedialog.askopenfilename()

    print("选择文献目录...")
    target_dir = filedialog.askdirectory()

    file_lt = os.listdir(target_dir)
    for f in file_lt:
        print(f)

    # 使用对话框询问是否执行下一步操作
    ask = tkinter.messagebox.askokcancel("确认",
                                         f"要将{target_dir}中的文件作为待看添加到markdown文档{md_path}中吗？")
    if ask is True:
        with open(md_path, "a", encoding="utf8") as md_f:
            file_lt = ["+ [ ] :bookmark:​" + f + "\n" for f in file_lt]  # 在文件前添加勾选框（和一个emoji
            md_f.writelines(file_lt)


if __name__ == '__main__':
    main()
