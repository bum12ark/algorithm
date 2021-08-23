"""
* 두수의 합
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

- Example
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx, value in enumerate(nums):
            nums_map[value] = idx

        for idx, value in enumerate(nums):
            if target - value in nums_map and nums_map[target - value] != idx:
                return [idx, nums_map[target - value]]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx, value in enumerate(nums):
            if target - value in nums_map:
                return [nums_map[target - value], idx]
            nums_map[value] = idx

if __name__ == '__main__':
    nums_1, target_1 = [2, 7, 11, 15], 9
    # print(Solution().twoSum(nums_1, target_1), [0, 1])
    nums_2, target_2 = [3, 2, 4], 6
    # print(Solution().twoSum(nums_2, target_2), [1, 2])
    nums_3, target_3 = [2, 5, 5, 11], 10
    print(Solution().twoSum(nums_3, target_3), [1, 2])

"""
[시작 체크 리스트]
[✓] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""
