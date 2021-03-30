"""
url: https://leetcode.com/problems/permutations/
* 순열
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.

- Example 1
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
- Example 2
Input: nums = [0,1]
Output: [[0,1],[1,0]]
- Example 3
Input: nums = [1]
Output: [[1]]
"""
from typing import List

import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev_element = []
        result = []

        def DFS(element):
            if len(element) == 0:
                result.append(prev_element.copy())
                return
            for num in element:
                next_element = element.copy()
                next_element.remove(num)
                prev_element.append(num)
                DFS(next_element)
                prev_element.pop()

        DFS(nums)
        return result

    def permute_itertools(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]), "||", [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    print(Solution().permute_itertools([1, 2, 3]), "||",
          [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[✓] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""