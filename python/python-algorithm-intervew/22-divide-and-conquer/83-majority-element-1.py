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
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num


if __name__ == '__main__':
    test_1 = [3, 2, 3]
    test_2 = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(test_2))
