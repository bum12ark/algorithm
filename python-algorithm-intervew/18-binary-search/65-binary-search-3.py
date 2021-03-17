"""
* 이진 검색
정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
"""
import bisect
from typing import List


class Solution:
    # 이진 검색 모듈
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))