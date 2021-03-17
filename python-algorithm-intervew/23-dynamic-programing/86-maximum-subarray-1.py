"""
* 최대 서브 배열
합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.
- Example
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] 은 합 6으로 가장 큰 서브 배열이다.
"""
from typing import List


class Solution:
    # 메모이 제이션
    def maxSubArray(self, nums: List[int]) -> int:
        sums: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))

        return max(sums)

    def maxSubArrayMine(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
    print(Solution().maxSubArrayMine(nums))