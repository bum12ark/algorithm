"""
출처: https://www.acmicpc.net/problem/18870
"""
import collections
from typing import List


def coordinate_mine(array: List[int], size: int):
    dic = collections.defaultdict(list)

    for idx, val in enumerate(nums):
        dic[val].append(idx)
    print(dic)
    result = [0] * size
    for idx, val in enumerate(sorted(set(nums))):
        while dic[val]:
            result[dic[val].pop()] = idx

    return result


def coordinate(array: List[int], size: int):
    dic = collections.defaultdict(list)

    for idx, val in enumerate(sorted(set(array))):
        dic[val] = idx

    result = []
    for num in array:
        result.append(dic[num])

    return result


if __name__ == '__main__':
    size = int(input())
    nums = list(map(int, input().split()))

    result = coordinate(nums, size)
    print(' '.join(map(str, result)))
