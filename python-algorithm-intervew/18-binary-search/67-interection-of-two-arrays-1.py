"""
* 두 배열의 교집합
두 배열의 교집합을 구하라.
- Example 1
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
- Example 2
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4]
"""
from typing import List


class Solution:
    # 부르트 포스 방식
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        return result


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    Solution().intersection(nums1, nums2)