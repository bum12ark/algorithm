"""
출처: https://www.acmicpc.net/problem/2156
"""
import collections

size = int(input())
wine = [int(input()) for _ in range(size)]

dp = collections.defaultdict(int)

if size == 1:
    print(wine[0])
elif size == 2:
    print(max(wine[0] + wine[1], wine[0]))
else:
    dp[0] = wine[0]
    dp[1] = max(wine[0] + wine[1], wine[0])
    dp[2] = max(dp[1], wine[2] + wine[0], wine[2] + wine[1])
    for i in range(3, size):
        dp[i] = max(
            # 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
            dp[i - 3] + wine[i - 1] + wine[i],
            # 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
            dp[i - 2] + wine[i],
            # 이번 포도주를 먹지 않아야 하는 경우
            dp[i - 1]
        )
    print(dp[size - 1])