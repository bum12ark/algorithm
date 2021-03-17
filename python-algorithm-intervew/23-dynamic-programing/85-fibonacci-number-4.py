"""
* 피보나치 수
피보나치 수를 구하라.
"""


class Solution:
    # 두 변수만 이용해 공간 절약
    def fib(self, n: int) -> int:
        x,  y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x


if __name__ == '__main__':
    print(Solution().fib(6))