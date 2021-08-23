"""
출처: https://www.acmicpc.net/problem/11054
"""

size = int(input())
nums = list(map(int, input().split()))

dp_H = [1] * size
dp_L = [1] * size

for i in range(size):
    for j in range(i):
        if nums[i] > nums[j]:
            dp_H[i] = max(dp_H[i], dp_H[j] + 1)

for i in range(size - 1, -1, -1):
    for j in range(size - 1, i, -1):
        if nums[i] > nums[j]:
            dp_L[i] = max(dp_L[i], dp_L[j] + 1)

result = []
for i in range(size):
    result.append(dp_H[i] + dp_L[i] - 1)

print(max(result))
