"""
출처: https://www.acmicpc.net/problem/1463
"""
import collections


def tabulation(n):
    dp = collections.defaultdict(int)
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + 1
        # 3으로 나눠 떨어질 경우
        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
        # 2로 나눠 떨어질 경우 else if가 아닌 if로 비교해야한다.
        # 모든 경우의 수에서 가장 작은 값을 구해야 하기 때문
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])

    return dp[n]


def memoization(n):
    dp = collections.defaultdict(int)
    if n <= 1:
        dp[n] = 0
        return 0
    elif n == 2 or n == 3:
        dp[n] = 1
        return 1

    if dp[n]:
        return dp[n]

    dp[n] = memoization(n - 1) + 1
    # 3으로 나눠 떨어질 경우
    if n % 3 == 0:
        dp[n] = min(memoization(n // 3) + 1, dp[n])
    # 2로 나눠 떨어질 경우
    if n % 2 == 0:
        dp[n] = min(memoization(n // 2) + 1, dp[n])

    return dp[n]


if __name__ == '__main__':
    param = int(input())
    # print(tabulation(param))
    print(memoization(param))
