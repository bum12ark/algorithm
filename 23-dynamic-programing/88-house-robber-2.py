"""
* 집 도둑
당신은 전문 털이범이다.
어느 집에서든 돈을 훔쳐올 수 있지만 경보 시스템 때문에 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 가능하다.
각 집에는 훔칠 수 있는 돈의 액수가 입력값으로 표기되어 있다.
훔칠 수 있는 가장 큰 금액을 출력하라.
- Example 1
Input: [1, 2, 3, 1]
Output: 4
Explanation: 첫 번째 집에서1, 세 번째 집에서 3, 따라서 1 + 3 = 4 이다.
- Example 2
Input: [2, 7, 9, 3, 1]
Output: 12
Explanation: 첫 번째 집에서 2, 세 번째 집에서 9, 다섯 번째 집에서 1, 따라서 2 + 9 + 1 = 12 이다.
- Example 3
Input: [2, 1, 1, 2]
Output: 4
Explanation: 첫 번째 집에서 2, 네 번째 집에서 2, 따라서 2 + 2 = 4 이다.
"""
import collections
from typing import List


class Solution:
    # 타뷸레이션
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1]


if __name__ == '__main__':
    test_1 = [1, 2, 3, 1]
    test_2 = [2, 7, 9, 3, 1]
    test_3 = [2, 1, 1, 2]
    print(Solution().rob([1, 4, 1]))