"""
출처: https://www.acmicpc.net/problem/1912
"""
import sys
from typing import List


def memoization(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

    return max(nums)


def kadane(nums: List[int]) -> int:
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum


if __name__ == '__main__':
    size = int(input())
    nums = list(map(int, input().split()))
    # print(memoization(nums))
    print(kadane(nums))
