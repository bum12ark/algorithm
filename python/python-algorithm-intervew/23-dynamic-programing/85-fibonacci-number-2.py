"""
* 피보나치 수
피보나치 수를 구하라.
"""
import collections


class Solution:
    dp = collections.defaultdict(int)

    # 메모이제이션 (하향식)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


if __name__ == '__main__':
    print(Solution().fib(6))