"""
출처: https://www.acmicpc.net/problem/7576
"""
import collections
import sys
from pprint import pprint


def bfs(x, y, arr):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    deq = collections.deque([(x, y)])
    while deq:
        px, py = deq.popleft()
        for idx in range(4):
            nx = px + dx[idx]
            ny = py + dy[idx]

            if 0 <= nx < N and \
                    0 <= ny < M and \
                    arr[nx][ny] == 0:
                arr[nx][ny] += arr[px][py] + 1
                deq.append((nx, ny))

    return arr


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())  # 가로 칸의 수, 세로 칸의 수

    box = [
        list(map(int, sys.stdin.readline().split())) for _ in range(N)
    ]

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:  # 익은 토마토인 경우 bfs 탐색 시작
                result = bfs(i, j, box)

    pprint(result)
    for row in result:
        if 0 in row:
            print(-1)

    print(max(map(max, result)) - 1)
