# -*- coding: utf-8 -*-
# @Time: 2020/4/29 23:32
# @Author: Rollbear
# @Filename: shortest_path.py

INFINITY = 65535


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
    d_0 = [[0, 8, INFINITY, 5, INFINITY, INFINITY, 6, INFINITY, INFINITY],
           [8, 0, 10, INFINITY, INFINITY, INFINITY, INFINITY, INFINITY, INFINITY],
           [INFINITY, 10, 0, INFINITY, 13, 13, INFINITY, INFINITY, INFINITY],
           [5, INFINITY, INFINITY, 0, 6, INFINITY, 7, 8, INFINITY],
           [INFINITY, INFINITY, 13, 6, 0, INFINITY, INFINITY, INFINITY, 12],
           [INFINITY, INFINITY, 13, INFINITY, INFINITY, 0, INFINITY, INFINITY, 15],
           [6, INFINITY, INFINITY, 7, INFINITY, INFINITY, 0, 11, INFINITY],
           [INFINITY, INFINITY, INFINITY, 8, INFINITY, INFINITY, 11, 0, 16],
           [INFINITY, INFINITY, INFINITY, INFINITY, 12, 15, INFINITY, 16, 0]]
    res = shortest_path_floyd(d_0)


if __name__ == '__main__':
    main()
