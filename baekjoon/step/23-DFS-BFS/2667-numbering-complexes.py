"""
출처: https://www.acmicpc.net/problem/2667
"""
import sys
from typing import List


class Solution:
    complex_number = 0  # 단지별 집 숫자
    complex_list = []  # 단지별 집 숫자를 저장하는 리스트

    def dfs(self, x, y, grid):
        if x < 0 or len(grid) <= x \
                or y < 0 or len(grid[x]) <= y \
                or grid[x][y] != 1:
            return

        grid[x][y] = 0
        # 단지 내의 집 개수 증가
        self.complex_number += 1

        self.dfs(x + 1, y, grid)
        self.dfs(x, y + 1, grid)
        self.dfs(x - 1, y, grid)
        self.dfs(x, y - 1, grid)

    def numbering(self, complexes: List[str]) -> int:
        if not complexes:
            return 0

        count = 0
        for i in range(len(complexes)):
            for y in range(len(complexes[i])):
                # 단지가 발견될 경우
                if complexes[i][y] == 1:
                    self.dfs(i, y, complexes)
                    # 육지 탐색 후 전체 카운트 증가
                    count += 1
                    # 단지별 숫자 카운트
                    self.complex_list.append(self.complex_number)
                    self.complex_number = 0
        return count


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    T = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    print(Solution().numbering(T))
    for n in sorted(Solution().complex_list):
        print(n)
