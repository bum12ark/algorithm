"""
* 과반수 엘리먼트
과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라.
- Example 1
Input: [3, 2, 3]
Output: 3
- Example 2
Input: [2, 2, 1, 1, 1, 2, 2]
Output: 2
"""
import collections
from typing import List


class Solution:
    # 파이썬다운 방식
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    test_1 = [3, 2, 3]
    test_2 = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(test_1))
