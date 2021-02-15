"""
* 주식을 사고팔기 가장 좋은 시점
한번의 거래로 낼 수 있는 최대 이익을 산출하라.
- 입력
[7, 1, 5, 3, 6, 4]
- 출력
5
"""
import sys
from typing import List


class Solution:
    # 저점과 고점 비교
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # 이익은 0이라고 가정하여 -sys.maxsize 대신 0을 초기화
        min_price = sys.maxsize

        # 최소값과 최대값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit



if __name__ == '__main__':
    solution = Solution()
    param = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(param))