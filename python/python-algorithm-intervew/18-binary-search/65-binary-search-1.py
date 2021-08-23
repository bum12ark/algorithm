"""
* 이진 검색
정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
"""
from typing import List


class Solution:
    # 재귀 풀이
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
        return binary_search(0, len(nums) - 1)



if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))