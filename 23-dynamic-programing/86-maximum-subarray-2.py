"""
* 최대 서브 배열
합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.
- Example
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] 은 합 6으로 가장 큰 서브 배열이다.
"""
import sys
from typing import List


class Solution:
    # 카데인 알고리즘
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))