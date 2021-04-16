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
        global flag
        # 탈출 조건 (1)
        if flag:
            return

        # 탈출 조건 (2)
        if index == len(zeros):
            flag = True
            for row in question:
                # asterisk Unpacking
                print(*row)
            return

        x, y = zeros[index]

        valuable = is_promising(x, y)
        for val in valuable:
            question[x][y] = val
            dfs(index + 1)
            # 유효하지 않을 경우 해당 값을 0으로 초기화
            question[x][y] = 0

    dfs(0)


if __name__ == '__main__':
    q = [list(map(int, input().split())) for _ in range(9)]
    z = [(i, j) for i in range(9) for j in range(9) if q[i][j] == 0]
    flag = False
    sudoku(q, z)
