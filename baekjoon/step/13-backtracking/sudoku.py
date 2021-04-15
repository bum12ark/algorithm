"""
출처: https://www.acmicpc.net/problem/2580
"""


def sudoku(question, zeros):
    def is_promising(x, y):
        numbers = list(range(1, 10))
        # 가로, 세로 판별
        for k in range(9):
            if question[x][k] in numbers:
                numbers.remove(question[x][k])
            if question[k][y] in numbers:
                numbers.remove(question[k][y])

        # 3 X 3 판별
        _i = x // 3
        _j = y // 3
        for i in range(_i * 3, (_i + 1) * 3):
            for j in range(_j * 3, (_j + 1) * 3):
                if question[i][j] in numbers:
                    numbers.remove(question[i][j])
        return numbers

    def dfs(index):
        # 탈출 조건
        if index == len(zeros):
            return

        x, y = zeros[index]
        print(x, y)

        valuable = is_promising(x, y)
        for val in valuable:
            question[x][y] = val
            dfs(index + 1)
            question[x][y] = 0

    dfs(0)


if __name__ == '__main__':
    q = [
        [0, 3, 5, 4, 6, 9, 2, 7, 8],
        [7, 8, 2, 1, 0, 5, 6, 0, 9],
        [0, 6, 0, 2, 7, 8, 1, 3, 5],
        [3, 2, 1, 0, 4, 6, 8, 9, 7],
        [8, 0, 4, 9, 1, 3, 5, 0, 6],
        [5, 9, 6, 8, 2, 0, 4, 1, 3],
        [9, 1, 7, 6, 5, 2, 0, 8, 0],
        [6, 0, 3, 7, 0, 1, 9, 5, 2],
        [2, 5, 8, 3, 9, 4, 7, 6, 0]
    ]
    z = [(i, j) for i in range(9) for j in range(9) if q[i][j] == 0]
    print(z)
    sudoku(q, z)
