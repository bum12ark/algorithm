"""
* 주식을 사고팔기 가장 좋은 시점
한번의 거래로 낼 수 있는 최대 이익을 산출하라.
- 입력
[7, 1, 5, 3, 6, 4]
- 출력
5
"""
from typing import List


class Solution:
    # 브루트 포스 방식 풀이
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_price = max(max_price,
                                prices[j] - prices[i])
        return max_price


if __name__ == '__main__':
    solution = Solution()
    param = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(param))