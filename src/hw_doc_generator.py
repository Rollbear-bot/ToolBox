# -*- coding: utf-8 -*-
# @Time: 2020/4/14 0:07
# @Author: Rollbear
# @Filename: hw_doc_generator.py

import tkinter
import os
# import docx  # 第三方库，读写word文档

from util import path
from tkinter import filedialog

from entity import document


def main():
    print("选择工作目录..")
    work_dir = filedialog.askdirectory()

    for file_name in os.listdir(work_dir):
        if file_name.endswith(".doc") or file_name.endswith(".docx"):
            # docx.
            pass


if __name__ == '__main__':
    main()
