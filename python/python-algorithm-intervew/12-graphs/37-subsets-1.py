"""
* 부분 집합
모든 부분 집합을 리턴하라.
- Example 1
Input : nums = [1, 2, 3]
Output : [
    [3],
    [1],
    [2],
    [1, 2, 3],
    [1, 3],
    [2, 3],
    [1, 2],
    [],
]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))