# -*- coding: utf-8 -*-
# @Time: 2020/3/13 15:24
# @Author: Rollbear
# @Filename: converter.py


from entity.topic import Topic


def scanner(p_lines: list):
    """
    Markdown格式解析器
    分析标题、子标题、正文之间的关系，构造一个树形结构
    :param p_lines: 以行为元素的列表
    :return: 解析产生的Topic对象
    """
    lines = p_lines.copy()
    root_topic = Topic(lines[0])  # 文件的第一行应当是主标题
    lines.remove(lines[0])

    cur_topic = root_topic
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
    return root_topic

