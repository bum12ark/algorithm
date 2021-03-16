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
    # 다이나믹 프로그래밍 풀이
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        # [분할]
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # [정복] True == 1, False == 0
        return [b, a][nums.count(a) > half]


if __name__ == '__main__':
    test_1 = [3, 2, 3]
    test_2 = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(test_1))
