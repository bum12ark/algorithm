"""
url: https://leetcode.com/problems/number-of-islands/
* 섬의 개수
1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을때, 섬의 개수를 계산하라.
(연결되어 있는 1의 덩어리 개수를 구하라.)

- Example 1
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
- Example 2
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(i, j):
            if i < 0 or i >= len(grid) \
                    or j < 0 or j >= len(grid[i]) \
                    or grid[i][j] != "1":
                return

            # 방문한 "1"을 "#"으로 변경 처리
            grid[i][j] = "#"

            # 동서남북으로 재귀 호출
            DFS(i, j - 1)
            DFS(i, j + 1)
            DFS(i - 1, j)
            DFS(i + 1, j)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    DFS(i, j)
                    count += 1

        return count


if __name__ == '__main__':
    grid_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    # print(Solution().numIslands(grid_1), "||", 1)
    grid_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid_2), "||", "?")
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[✓] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""
