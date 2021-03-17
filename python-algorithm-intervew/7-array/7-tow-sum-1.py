"""
[두수의 합]
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

- 입력
nums = [2, 7, 11, 15], target = 9
- 출력
[0,1]
"""
import collections
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target - n], i]
            nums_map[n] = i



if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))
