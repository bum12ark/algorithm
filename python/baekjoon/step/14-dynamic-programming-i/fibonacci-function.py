"""
출처: https://www.acmicpc.net/problem/1003
"""

import collections


# 메모이제이션
def fib_memoization(n: int):
    if n <= 1:
        dp[n] = n
        return n

    if dp[n]:
        return dp[n]
    dp[n] = fib_memoization(n - 1) + fib_memoization(n - 2)

    return dp[n]


# 타뷸레이션
def fib_tabulation(n: int):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    size = int(input())
    dp = collections.defaultdict(int)

    for _ in range(size):
        case = int(input())
        if case == 0:
            print(1, 0)
        else:
            fib = fib_tabulation(case)
            # 사용 횟수 출력
            print(dp[case - 1], dp[case])
