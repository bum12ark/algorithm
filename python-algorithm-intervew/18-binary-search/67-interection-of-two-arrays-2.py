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
    # 이진 검색 (직접 구현)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        nums2.sort()
        for n1 in nums1:
            left, right = 0, len(nums2) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums2[mid] < n1:
                    left = mid + 1
                elif nums2[mid] > n1:
                    right = mid - 1
                else:
                    break
            if n1 == nums2[mid]:
                result.add(n1)
        return result

    # 이진 검색 (모듈 사용)
    def intersection_bisect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        nums2.sort()
        for n1 in nums1:
            mid = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > mid and n1 == nums2[mid]:
                result.add(n1)
        return result


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1, nums2))
    print(Solution().intersection_bisect(nums1, nums2))