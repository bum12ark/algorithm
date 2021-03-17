"""
* 피보나치 수
피보나치 수를 구하라.
"""
import collections


class Solution:
    dp = collections.defaultdict(int)

    # 타뷸레이션 (상향식)
    def fib(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]


if __name__ == '__main__':
    print(Solution().fib(6))