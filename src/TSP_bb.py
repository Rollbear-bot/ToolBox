# -*- coding: utf-8 -*-
# @Time: 2020/5/28 9:20
# @Author: Rollbear
# @Filename: TSP_bb.py
# TSP: branch and bound method

MAXINT = 65563


def calc_bound(matrix: list):
    """
    calculate the bound of matrix
    :param matrix: linking information
    :return: tuple(bound, simplified matrix)
    """
    # deep copy
    m = [row.copy() for row in matrix]
    bound = 0

    # check that if each row has a "0"(at least)
    for row_index, row in enumerate(m):
        if 0 not in row:
            min_item = min(row)
            bound += min_item
            # each item in current row minus the min_item
            for item_index, item in enumerate(m[row_index]):
                m[row_index][item_index] -= min_item

    # check that if each column has a "0"(at least)
    for col_index in range(len(m)):
        cur_col = [row[col_index] for row in m]
        if 0 not in cur_col:
            min_item = min(cur_col)
            bound += min_item
            # each item in cur_col minus the min_item
            for row_index, row in enumerate(m):
                m[row_index][col_index] -= min_item
    return bound, m


def sort_edges(e_lt: list):
    """
    sort edges in connectable order
    :param e_lt: list of tuple(edge)
    :return: sorted edges list
    """
    swap_flag = False
    edges = e_lt.copy()
    for flag in range(len(edges)-1):
        for index in range(flag+1, len(edges)):
            if edges[flag][1] == edges[index][0] and index != flag+1:
                edges[flag+1], edges[index] = edges[index], edges[flag+1]  # swap
                swap_flag = True
                break
    # to avoid being stuck,
    # if items have never been swapped, inverse the list and try again
    if len(edges) >= 2 and edges[0][1] != edges[1][0]:
        return sort_edges(e_lt[-1::-1])
    return edges


def tsp_bb(matrix: list):
    """
    traveling salesman problem: branch and bound method
    :param matrix: linking info of a graph, 2d adjacency matrix
    :return: optimal solution and bound
    """
    # initialization
    col_id = list(range(1, len(matrix) + 1))  # mark the remaining cols
    cur_bound, cur_mat = calc_bound(matrix)
    edges = []
    row_flag = 1

    while len(cur_mat) > 0:
        row_index = 0
        col_index = cur_mat[row_index].index(0)

        # pop a row and a column from current matrix
        # the new matrix become a child_node
        left_child = [row.copy() for row in cur_mat]  # make a copy of cur_mat
        left_child.pop(row_index)
        for row_i, _ in enumerate(left_child):
            left_child[row_i].pop(col_index)
        lc_col_id = col_id.copy()
        lc_col_id.pop(col_index)  # remove the column id

        lc_edges = edges.copy()
        lc_edges.append((row_flag, col_id[col_index]))

        # block some edges in order to avoid making loops
        lc_edges = sort_edges(lc_edges)
        if row_flag < 3:
            for edge in [(edge[1], lc_edges[0][0]) for edge in lc_edges[-1::-1]]:
                r = edge[0] - row_flag - 1
                try:
                    c = lc_col_id.index(edge[1])
                except ValueError:
                    c = -1
                if r >= 0 and c != -1:
                    left_child[r][c] = MAXINT

        left_child_bound, left_child = calc_bound(left_child)

        right_child = [row.copy() for row in cur_mat]  # make a copy of cur_mat
        right_child[row_index][col_index] = MAXINT
        right_child_bound, right_child = calc_bound(right_child)

        # minimize the bound, choice the min_bound branch
        if left_child_bound < right_child_bound:
            # update column id
            col_id = lc_col_id.copy()
            # record the invalid edge
            edges = lc_edges.copy()
            row_flag += 1

            cur_bound += left_child_bound
            cur_mat = left_child

        else:
            cur_bound += right_child_bound
            cur_mat = right_child

    return edges, cur_bound


def main():
    m = [[MAXINT, 17, 7, 35, 18],
         [9, MAXINT, 5, 14, 19],
         [29, 24, MAXINT, 30, 12],
         [27, 21, 25, MAXINT, 48],
         [15, 16, 28, 18, MAXINT]]

    solution, bound = tsp_bb(m)

    print(f"the optimal solution is {solution}")
    print(f"the travel path is {[edge[0] for edge in sort_edges(solution)]}")
    print(f"the final bound is {bound}")


if __name__ == '__main__':
    main()
