# -*- coding: utf-8 -*-
# @Time: 2020/5/27 11:23
# @Author: Rollbear
# @Filename: k_queens.py
# k皇后问题（回溯法）


def valid_board(c: list, row_length: int):
    """
    check that if the board is valid
    :param c: location vector of the queens on the board
    :param row_length: length of row on the chess board
    :return: BOOLEAN value or STRING "partial solution"
    """
    tmp = c.copy()
    if 0 in tmp:
        tmp = tmp[:tmp.index(0)]  # clear the "0" (unsettled rows)

    # value in the list must be unique
    if len(set(tmp)) != len(tmp):
        return False

    for row_id, location in enumerate(tmp):
        # for each row, check the next line and the below
        for index in range(row_id+1, len(c)):
            delta = index - row_id
            if location + delta <= row_length:
                if c[index] == location + delta:
                    return False
            if location - delta > 0:
                if c[index] == location - delta:
                    return False
    if 0 in c:
        return "partial solution"  # the partial solution is found, continue
    return True  # one of the final solutions is found


def k_queens(n_queens: int):
    """
    k queens problems
    :param n_queens: number of queens
    :return: solutions, queens' location on each row
    """
    res = []  # array of solutions of the problem
    # init a array, location of the queens on the rows of the board
    c = list(range(n_queens))
    for k in range(1, n_queens+1):
        c[k-1] = 0  # no any queen on the board
    # flag = False  # notice that if the solution is found

    k = 1  # row id
    while k >= 1:
        while c[k-1] <= n_queens-1:
            c[k-1] = c[k-1] + 1
            if valid_board(c, row_length=n_queens) is True:
                res.append(c.copy())  # one of the final solutions
            if valid_board(c, row_length=n_queens) == "partial solution":
                k += 1  # go forward
                continue
        c[k-1] = 0  # clear the choice on current row
        k -= 1  # traceback

    return res


def main():
    res = k_queens(n_queens=4)
    print(f"number of solutions: {len(res)}")
    for r in res:
        print(r)


if __name__ == '__main__':
    main()
