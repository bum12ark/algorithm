"""
출처: https://www.acmicpc.net/problem/1012
"""
import collections
import sys
from typing import List


def dfs(x: int, y: int, grid: List[int]) -> None:
    # 탈출 조건
    if x < 0 or x >= len(grid) \
            or y < 0 or y >= len(grid[x]) \
            or grid[x][y] != 1:
        return

    grid[x][y] = 0  # 방문 표시

    # 동서남북 탐색
    dfs(x + 1, y, grid)
    dfs(x, y + 1, grid)
    dfs(x - 1, y, grid)
    dfs(x, y - 1, grid)


def bfs(x: int, y: int, grid: List[int]) -> None:
    ewsn_x = [1, -1, 0, 0]  # 동서남북 x
    ewns_y = [0, 0, 1, -1]  # 동서남북 y

    deq = collections.deque([(x, y)])
    while deq:
        pop_x, pop_y = deq.popleft()
        for idx in range(4):
            row = pop_x + ewsn_x[idx]
            col = pop_y + ewns_y[idx]

            # 진행 조건
            if 0 <= row < len(grid) and \
                    0 <= col < len(grid[row]) and \
                    grid[row][col] == 1:
                grid[row][col] = 0  # 방문 표시
                deq.append((row, col))


def nums_cabbage(grid: List[int]) -> int:
    # 예외 처리
    if not grid:
        return 0

    count = 0  # 배추흰지렁이 마리 수
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # dfs(i, j, grid)
                bfs(i, j, grid)
                # 모든 배추밭 탐색 후 카운트 증가
                count += 1
    return count


if __name__ == '__main__':
    # 런타임 에러 방지 (최대 재귀 허용 횟수)
    sys.setrecursionlimit(10000)
    T = int(sys.stdin.readline())  # 테스트 케이스 개수
    for _ in range(T):
        # 가로길이, 세로길이, 배추 위치 개수
        M, N, K = map(int, sys.stdin.readline().split())

        field = [[0 for _ in range(M)] for y in range(N)]

        # 배추 위치 초기화
        for _ in range(K):
            a, b = map(int, sys.stdin.readline().split())
            field[b][a] = 1

        print(nums_cabbage(field))

"""
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
"""
