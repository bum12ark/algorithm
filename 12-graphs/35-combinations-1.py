"""
* 조합
전체 수 n을 입력받아 k개의 조합을 리턴하라
- Example 1
Input : n = 4, k = 2
Output :
[
    [2, 4],
    [3, 4],
    [2, 3],
    [1, 2],
    [1, 3],
    [1, 4]
]
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[str]]:
        result = []

        def dfs(element, start: int, k: int):
            if k == 0:
                result.append(element[:])

            for i in range(start, n + 1):
                element.append(i)
                dfs(element, i + 1, k - 1)
                element.pop()

        dfs([], 1, k)
        return result



if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
