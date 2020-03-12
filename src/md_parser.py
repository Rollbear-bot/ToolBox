# markdown分析器
import tkinter
from tkinter import filedialog


class Topic(object):
    """主题"""
    def __init__(self, raw_title: str):
        self.raw_title = raw_title  # 标题（带井号和空格的md格式标题）
        self.title = raw_title.split(' ')[1]  # 提取标题文本
        self.sub_topic = []  # 该标题下的子标题
        self.text = []  # 该标题下的正文（非其他子标题下）
        # 分析标题等级，顶级标题level=1
        self.level = raw_title.split(' ')[0].count('#')

    # @staticmethod
    def scanner(self, it: iter):
        """扫描该标题下的所有子标题和正文，
        直到遇到下一个同级标题"""
        for line in it:
            if line.startswith('#'):
                cur_topic = Topic(line)
                # 若扫描到同级或更高级标题，弹出
                if cur_topic.level >= self.level:
                    # 返回迭代器和扫描到的同级标题
                    return it, cur_topic
                # 否则成为当前标题的子标题
                self.sub_topic.append(Topic(line))
            else:
                # 不是标题的部分加入正文
                self.text.append(line)
        return None


def scanner_2(self, headline: Topic, lines: list):
    stack = [headline, ]  # 标题栈
    cur_topic = headline
    parent_topic = None  # 父级标题
    lines.remove(headline.raw_title)

    for line in lines:
        if line.startswith('#'):
            temp = Topic(line)
            if temp.level > cur_topic.level:
                # 扫描到子标题，将它添加到子标题表
                cur_topic.sub_topic.append(temp)
                stack.append(cur_topic)  # 压栈
                parent_topic = cur_topic  # 标记父级标题
                cur_topic = temp  # 话题指针移动到子标题

            elif temp.level == cur_topic.level:
                # 扫描到同级标题，更新父级标题的子标题表
                parent_topic.sub_topic.append(temp)
                cur_topic = temp  # 话题指针移动到新标题

            else:
                # 扫描到高级标题，退栈
                topic_level = temp.level
                while cur_topic.level >= topic_level:
                    # 找到该高级标题的上一级标题
                    cur_topic = stack.pop()
                cur_topic.sub_topic.append(temp)

        else:
            # 这一行的内容加入当前主题的正文部分
            cur_topic.text.append(line)


def main():
    root = tkinter.Tk()
    root.withdraw()

    # 打开一个md文件
    file_path = filedialog.askopenfilename()
    while not str(file_path).endswith('.md'):
        print('你打开的不是markdown文件，请重新选择')
        file_path = filedialog.askopenfilename()

    md_the_file = open(file_path, 'r', encoding='utf8')  # 以只读方式打开
    lines = iter(md_the_file.readlines())  # 将列表转化为迭代器
    for line in lines:
        # 主标题
        headline = Topic(line)
        while not lines.__next__() is None:
            lines, sub = headline.scanner(lines)
            sub.scanner(lines)

    print("hello")


if __name__ == '__main__':
    main()

