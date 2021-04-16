"""
출처: https://www.acmicpc.net/problem/2579
"""
import collections

size = int(input())
stair = [int(input()) for _ in range(size)]

dp = collections.defaultdict(int)

if size == 1:
    print(stair[0])
elif size == 2:
    print(max(stair[0] + stair[1], stair[1]))
elif size == 3:
    print(max(stair[1] + stair[2], stair[0] + stair[2]))
else:
    dp[0] = stair[0]
    dp[1] = max(stair[0] + stair[1], stair[1])
    dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

    for i in range(3, len(stair)):
        dp[i] = max(
            dp[i - 2] + stair[i],
            dp[i - 3] + stair[i - 1] + stair[i]
        )

    print(dp[size - 1])