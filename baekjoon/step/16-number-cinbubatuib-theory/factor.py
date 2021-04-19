"""
출처: https://www.acmicpc.net/problem/1037
"""

size = int(input())
nums = list(map(int, input().split()))

nums.sort()
print(nums[0] * nums[size - 1])
