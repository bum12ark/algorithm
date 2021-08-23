"""
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
* 주식을 사고팔기 가장 좋은 시점
한번의 거래로 낼 수 있는 최대 이익을 산출하라.

- Example
Input: prices = [7,1,5,3,6,4]
Output: 5
"""
import sys
from typing import List


# 카데인 알고리즘
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        _min = sys.maxsize
        for idx, value in enumerate(prices):
            _min = min(_min, value)
            _max = max(_max, value - _min)
        return _max


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]), "||", 5)
    print(Solution().maxProfit([7, 6, 4, 3, 1]), "||", 0)
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[✓] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""