"""
출처: https://www.acmicpc.net/problem/2178
"""
import collections
import sys

N, M = map(int, sys.stdin.readline().split())
maze = [
    list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)
]

# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x: int, y: int) -> int:
    deq = collections.deque([(x, y)])  # bfs를 위한 데크
    discovered = [(x, y)]  # 방문 여부를 위한 리스트
    while deq:
        x, y = deq.popleft()
        # 탈출 조건 (출구 도착)
        if x == N - 1 and \
                y == M - 1:
            return maze[x][y]
        for idx in range(4):  # 동서남북 탐색
            nx = x + dx[idx]
            ny = y + dy[idx]

            # 진행 조건
            if 0 <= nx < len(maze) and \
                    0 <= ny < len(maze[nx]) and \
                    maze[nx][ny] == 1 and \
                    (nx, ny) not in discovered:
                # 이전 경로에서 1 증가
                maze[nx][ny] = maze[x][y] + 1
                deq.append((nx, ny))


dfs_discovered = []


def dfs(x, y, prev_val):
    if x < 0 or x >= len(maze) or \
            y < 0 or y >= len(maze[x]) or \
            maze[x][y] != 1 or (x, y) in dfs_discovered:
        return

    maze[x][y] = prev_val + 1
    dfs_discovered.append((x, y))

    dfs(x - 1, y, maze[x][y])  # 밑
    dfs(x + 1, y, maze[x][y])  # 위
    dfs(x, y - 1, maze[x][y])  # 좌
    dfs(x, y + 1, maze[x][y])  # 우


if __name__ == '__main__':
    bfs(0, 0)  # 시작지점
    # dfs(0, 0, 0)
    for m in maze:
        print(m)
