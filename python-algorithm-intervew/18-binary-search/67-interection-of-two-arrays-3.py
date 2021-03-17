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
import bisect
from typing import List


class Solution:
    # 투 포인터로 구현
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1.sort()
        nums2.sort()

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1, nums2))
