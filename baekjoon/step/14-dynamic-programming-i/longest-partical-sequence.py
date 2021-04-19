"""
출처: https://www.acmicpc.net/problem/11053
"""

size = int(input())
nums = list(map(int, input().split()))

dp = [1] * size

for i in range(1, size):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
