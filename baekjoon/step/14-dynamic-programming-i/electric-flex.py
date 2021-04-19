"""
출처: https://www.acmicpc.net/problem/2565
"""

size = int(input())
nums = [list(map(int, input().split())) for _ in range(size)]

nums.sort(key=lambda x: x[0])

__to = [nums[i][1] for i in range(size)]
dp = [1] * size

for i in range(size):
    for j in range(i):
        if __to[i] > __to[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# b 전봇대에서 가장 긴 증가하는 부분수열을 빼주면 된다.
print(size - max(dp))
