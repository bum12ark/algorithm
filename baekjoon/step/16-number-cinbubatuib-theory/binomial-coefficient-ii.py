"""
출처: https://www.acmicpc.net/problem/11051
"""

import collections
import sys

dp = collections.defaultdict(int)
f_dp = collections.defaultdict(int)


def factorial(n: int) -> int:
    if f_dp[n]:
        return f_dp[n]

    f_dp[0] = 1
    for i in range(1, n + 1):
        f_dp[i] = f_dp[i - 1] * i
    return f_dp[i]


def combination(n: int, r: int) -> int:
    if dp[(n, r)]:
        return dp[(n, r)]

    if n == r or r == 0:
        dp[(n, r)] = 1
        return dp[(n, r)]

    dp[(n, r)] = (factorial(n) // (factorial(r) * factorial(n - r))) % 10007
    return dp[(n, r)]


if __name__ == '__main__':
    n, r = map(int, sys.stdin.readline().rstrip().split())
    print(combination(n, r))
