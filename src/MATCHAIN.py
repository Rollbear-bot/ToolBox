# -*- coding: utf-8 -*-
# @Time: 2020/4/30 7:35
# @Author: Rollbear
# @Filename: MATCHAIN.py
# 矩阵链相乘（组合优化问题）


def mat_chain(mat_size: list, path=False):
    """矩阵链相乘"""
    n = len(mat_size)  # 矩阵的个数，也是记录表的维度
    r = [mat[1] for mat in mat_size]
    r.insert(0, mat_size[0][0])  # 构造r

    # 填表
    d = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i, j] = 0

    for diff in range(1, n):  # 差值从1到n-1
        for i in range(1, n-diff+1):
            # index = [(i, k-1) for k in range(i+1, i+diff+1)]
            # index = sorted(index,
            #                key=lambda t: d[t[0], t[1]] + d[t[1]+1, t[0]+diff] + r[t[0]-1] * r[t[1]] * r[t[0]+diff])
            if path is False:
                d[i, i+diff] = min([d[i, k-1] + d[k, i+diff] + r[i-1] * r[k-1] * r[i+diff]
                                    for k in range(i+1, i+diff+1)])
            else:
                pass
                # d[i, i+diff] = index[0]
    # 输出表到控制台
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(str(d[i, j]).center(5, " "), end=" ")
        print()
    return d


def main():
    mat_size = [[2, 3],
                [3, 5],
                [5, 2],
                [2, 3],
                [3, 10],
                [10, 2]]
    res = mat_chain(mat_size)


if __name__ == '__main__':
    main()
