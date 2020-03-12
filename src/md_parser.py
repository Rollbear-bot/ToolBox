# markdown分析器
import tkinter
from tkinter import filedialog


class Topic(object):
    """主题"""
    def __init__(self, raw_title: str):
        self.raw_title = raw_title  # 标题（带井号和空格的md格式标题）
        self.title = raw_title.split(' ')[1][:-1]  # 提取标题文本
        self.sub_topic = []  # 该标题下的子标题
        self.parent_topic = None  # 父级标题
        self.text = []  # 该标题下的正文（非其他子标题下）
        # 分析标题等级，顶级标题level=1
        self.level = raw_title.split(' ')[0].count('#')

    def __str__(self):
        return self.title + f"（{self.level}级标题）"


def scanner(headline: Topic, lines: list):
    cur_topic = headline
    lines.remove(headline.raw_title)

    for line in lines:
        if line.startswith('#'):
            temp = Topic(line)
            if temp.level > cur_topic.level:
                # 扫描到子标题，将它添加到子标题表
                cur_topic.sub_topic.append(temp)
                temp.parent_topic = cur_topic

                cur_topic = temp  # 话题指针移动到子标题

            elif temp.level == cur_topic.level:
                # 扫描到同级标题，更新父级标题的子标题表
                cur_topic.parent_topic.sub_topic.append(temp)
                temp.parent_topic = cur_topic.parent_topic
                cur_topic = temp  # 话题指针移动到新标题

            else:
                # 扫描到高级标题，退栈
                topic_level = temp.level
                # 回溯到该标题的同级标题
                while cur_topic.level > topic_level:
                    cur_topic = cur_topic.parent_topic
                # 链入沟通父级标题的子标题表
                cur_topic.parent_topic.sub_topic.append(temp)
                temp.parent_topic = cur_topic.parent_topic
                cur_topic = temp

        else:
            # 这一行的内容加入当前主题的正文部分
            cur_topic.text.append(line)
    return headline


def main():
    root = tkinter.Tk()
    root.withdraw()

    # 打开一个md文件
    file_path = filedialog.askopenfilename()
    while not str(file_path).endswith('.md'):
        print('你打开的不是markdown文件，请重新选择')
        file_path = filedialog.askopenfilename()

    md_the_file = open(file_path, 'r', encoding='utf8')  # 以只读方式打开

    lines = md_the_file.readlines()
    result = scanner(Topic(lines[0]), lines)
    print("hello")


if __name__ == '__main__':
    main()

