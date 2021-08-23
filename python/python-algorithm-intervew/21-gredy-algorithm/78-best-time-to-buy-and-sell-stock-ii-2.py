"""
* 주식을 사고팔기 가장 좋은 시점 II
여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
- Example
Input: [7, 1, 5, 3, 6, 4]
Output: 7
Explanation: 1일 때 사서 5일 때 팔아 4의 이익을 얻고, 3일 때 사서 6일 때 팔아 3의 이익을 얻는다.
             둘을 합하면 7이 된다.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


if __name__ == '__main__':
    param = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(param))