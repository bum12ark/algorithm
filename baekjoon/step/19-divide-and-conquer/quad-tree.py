"""
출처: https://yabmoons.tistory.com/450
"""
import sys

N = int(sys.stdin.readline())
M = [
    list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)
]


def DFS(x, y, size):
    color = M[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != M[i][j]:
                print('(', end='')
                DFS(x, y, size // 2)
                DFS(x, y + size // 2, size // 2)
                DFS(x + size // 2, y, size // 2)
                DFS(x + size // 2, y + size // 2, size // 2)
                print(')', end='')
                return
    if color == 0:
        print(0, end='')
        return
    else:
        print(1, end='')
        return


DFS(0, 0, N)
