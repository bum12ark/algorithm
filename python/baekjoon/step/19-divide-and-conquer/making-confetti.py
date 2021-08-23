"""
출처: https://www.acmicpc.net/problem/2630
"""
import sys

N = int(sys.stdin.readline())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []


def divide_conquer(x, y, size):
    color = M[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            # 첫 색상과 다르다면 분할 시작
            if color != M[i][j]:
                divide_conquer(x, y, size // 2)  # 1사분면
                divide_conquer(x, y + size // 2, size // 2)  # 2사분면
                divide_conquer(x + size // 2, y, size // 2)  # 3사분면
                divide_conquer(x + size // 2, y + size // 2, size // 2)  # 4사분면
                return

    # 색상이 모두 같다면
    if color == 1:
        result.append(1)
        return
    else:
        result.append(0)
        return


divide_conquer(0, 0, N)
print(result.count(0))  # 흰 색종이
print(result.count(1))  # 파란 색종이
