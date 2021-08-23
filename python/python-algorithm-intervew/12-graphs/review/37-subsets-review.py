"""
url:
* 부분 집합
모든 부분 집합을 리턴하라.

- Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
- Example 2:
Input: nums = [0]
Output: [[],[0]]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def DFS(start, path):
            result.append(path)
            for idx in range(start, len(nums)):
                DFS(idx + 1, path + [nums[idx]])

        DFS(0, [])
        return result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]), "||", [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
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