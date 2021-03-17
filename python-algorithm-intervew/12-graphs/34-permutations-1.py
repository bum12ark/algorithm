"""
* 순열
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
- Example 1
Input : [1, 2, 3]
Output :
[
    [1, 2, 3],
    [1, 3, 2],
    [2 ,1 ,3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
