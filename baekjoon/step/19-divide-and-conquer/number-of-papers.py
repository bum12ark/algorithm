"""
출처: https://www.acmicpc.net/problem/1780
"""
import sys

N = int(sys.stdin.readline())
M = [
    list(map(int, sys.stdin.readline().split())) for _ in range(N)
]

result = []


def DFS(x, y, n):
    color = M[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != M[i][j]:
                DFS(x, y, n // 3)
                DFS(x, y + n // 3, n // 3)
                DFS(x, y + n // 3 + n // 3, n // 3)
                DFS(x + n // 3, y, n // 3)
                DFS(x + n // 3, y + n // 3, n // 3)
                DFS(x + n // 3, y + n // 3 + n // 3, n // 3)
                DFS(x + n // 3 + n // 3, y, n // 3)
                DFS(x + n // 3 + n // 3, y + n // 3, n // 3)
                DFS(x + n // 3 + n // 3, y + n // 3 + n // 3, n // 3)
                return

    if color == -1:
        result.append(-1)
        return
    elif color == 0:
        result.append(0)
        return
    elif color == 1:
        result.append(1)
        return


DFS(0, 0, N)

print(result.count(-1))
print(result.count(0))
print(result.count(1))
