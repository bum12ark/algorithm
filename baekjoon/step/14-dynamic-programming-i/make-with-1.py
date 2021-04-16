"""
출처:
"""
import collections


def tabulation(n):
    dp = collections.defaultdict(int)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 1):
        # 3으로 나눠 떨어질 경우
        if i % 3 == 0:
            dp[i] = dp[i / 3] + 1
        # 2로 나눠 떨어질 경우
        elif i % 2 == 0:
            dp[i] = dp[i / 2] + 1
        else:
            dp[i] = dp[i - 1] + 1

    return dp[n]


def memoization(n):
    dp = collections.defaultdict(int)
    if n == 1:
        dp[n] = 0
        return 0
    elif n == 2 or n == 3:
        dp[n] = 1
        return 1

    if dp[n]:
        return dp[n]

    # 3으로 나눠 떨어질 경우
    if n % 3 == 0:
        dp[n] = memoization(n / 3) + 1
    # 2로 나눠 떨어질 경우
    elif n % 2 == 0:
        dp[n] = memoization(n / 2) + 1
    else:
        dp[n] = memoization(n - 1) + 1

    return dp[n]


if __name__ == '__main__':
    param = 6
    print(tabulation(param))
    # print(memoization(param))
