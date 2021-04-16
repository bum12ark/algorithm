"""
출처: https://www.acmicpc.net/problem/9663
"""
from typing import List

count = 0


def n_queens(y: int, col: List[int]):
    n = len(col)

    # 탈출문
    if y == n:
        # print(col)
        global count
        count += 1
        return

    for x in range(n):
        col[y] = x
        if promising(y, col):
            n_queens(y + 1, col)

    return count


def promising(y: int, col: List[int]):
    for x in range(y):
        if col[y] == col[x] or abs(col[y] - col[x]) == (y - x):
            return False
    return True


if __name__ == '__main__':
    N = int(input())
    col = [0] * N
    print(n_queens(0, col))
