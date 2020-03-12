# markdown分析器
import tkinter
from tkinter import filedialog


class Topic(object):
    """主题类"""
    def __init__(self, raw_title: str):
        self.raw_title = raw_title  # 标题（带井号和空格的md格式标题）
        self.title = raw_title[raw_title.find(' ')+1:-1]  # 提取标题文本
        self.sub_topic = []  # 该标题下的子标题
        self.parent_topic = None  # 父级标题
        self.text = []  # 该标题下的正文（非其他子标题下）
        # 分析标题等级，顶级标题level=1
        self.level = raw_title.split(' ')[0].count('#')

    def __str__(self):
        return self.title + f"（{self.level}级标题）"


def scanner(md_file: open):
    """
    Markdown格式解析器
    分析标题、子标题、正文之间的关系，构造一个树形结构
    :param md_file: open方法返回的一个文本文件
    :return: 解析产生的Topic对象
    """
    lines = md_file.readlines()
    headline = Topic(lines[0])  # 文件的第一行应当是主标题
    lines.remove(lines[0])

    cur_topic = headline
    for line in lines:
        if line.startswith('#') and line.find(' ') != -1:
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
    # 解析完成，返回一个Topic对象
    return headline


def topic_list(headline: Topic):
    """展示当前标题以及它的所有下级标题
    树的递归前序遍历"""
    if len(headline.sub_topic) == 0:
        print('\t'*(headline.level-1) + str(headline))
        return None
    print('\t'*(headline.level-1) + str(headline))
    # 对子节点递归
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
    topic_list(result)


if __name__ == '__main__':
    main()

