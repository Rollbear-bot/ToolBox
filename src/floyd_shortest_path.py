# -*- coding: utf-8 -*-
# @Time: 2020/4/29 23:32
# @Author: Rollbear
# @Filename: shortest_path.py


def shortest_path_floyd(d_0: list):
    """弗洛伊德算法，点对最短路径问题"""
    n = len(d_0)  # n表示图中的节点个数

    # 将矩阵转化为映射表
    d_cur = {key: value for key, value in [((i, j), d_0[i-1][j-1])
                                           for i in range(1, n+1) for j in range(1, n+1)]}
    for k in range(1, n+1):
        # 矩阵迭代
        d_pre = d_cur.copy()
        d_cur = {}
        # 循环次数等于图中节点个数
        for i in range(1, n+1):
            for j in range(1, n+1):
                d_cur[i, j] = min((d_pre[i, j], d_pre[i, k] + d_pre[k, j]))
        # 输出当前矩阵
        print(f"D{k}:")
        for i in range(1, n+1):
            for j in range(1, n+1):
                print(str(d_cur[i, j]).center(5, " "), end=" ")
            print()
        print("-------------------------------")

    # 返回d_n
    return d_cur


def main():
    # 使用65535表示无穷大
    d_0 = [[0, 7, 6, 1],
           [65535, 0, 65535, 9],
           [1, 65535, 0, 65535],
           [4, 4, 2, 0]]
    res = shortest_path_floyd(d_0)


if __name__ == '__main__':
    main()
