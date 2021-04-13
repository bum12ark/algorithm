"""
출처: https://www.acmicpc.net/problem/2108
"""
import sys
from collections import Counter
from typing import List


def _average(nums: List[int], size: int):
    return round(sum(nums) / size)


def _median(nums: List[int], size: int):
    return sorted(nums)[size // 2]


def _lowest_value(nums: List[int], size: int):
    if size == 1:
        return nums[0]
    counter = Counter(sorted(nums)).most_common(2)
    return counter[1][0] if counter[0][1] == counter[1][1] else counter[0][0]


def _range(nums: List[int]):
    return max(nums) - min(nums)


if __name__ == '__main__':
    S = int(sys.stdin.readline())
    N = [int(sys.stdin.readline()) for _ in range(S)]
    print(_average(N, S))
    print(_median(N, S))
    print(_lowest_value(N, S))
    print(_range(N))
