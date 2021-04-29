"""
출처: https://www.acmicpc.net/problem/1920
"""
import sys
from typing import List


# 재귀 시간 초과
def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
    if left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            return binary_search(nums, target, mid + 1, right)
        elif nums[mid] > target:
            return binary_search(nums, target, left, mid - 1)
    else:  # 찾는 값이 없는 경우
        return 0


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    N_list = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    M_list = list(map(int, sys.stdin.readline().split()))

    N_list.sort()
    for m in M_list:
        print(binary_search(N_list, m, 0, N - 1))

