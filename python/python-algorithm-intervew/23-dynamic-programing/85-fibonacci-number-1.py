"""
* 피보나치 수
피보나치 수를 구하라.
"""


class Solution:
    # 부르트 포스 방식
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    print(Solution().fib(6))