"""
출처: https://www.acmicpc.net/problem/2805
"""
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))


def cut(left, right):
    if left <= right:
        mid = left + (right - left) // 2
        take = sum([t - mid for t in trees if t > mid])
        if take < M:
            return cut(left, mid - 1)
        else:
            return cut(mid + 1, right)
    return right


result = 0


def lower_bound(left, right):
    global result
    while left <= right:
        mid = left + (right - left) // 2
        take = sum([t - mid for t in trees if t > mid])
        # 만약 가져갈 나무가 적다면 길이를 적게 설정
        if take < M:
            right = mid - 1
        # 만약 가져갈 나무가 같거나 크다면 길이를 크게 설정하여 길이의 최댓값 산출
        else:
            left = mid + 1
            result = max(result, mid)
    return result


# print(cut(0, max(trees)))
print(lower_bound(0, max(trees)))
""" 
4 7
20 15 10 17
"""
