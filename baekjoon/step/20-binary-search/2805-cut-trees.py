"""
출처: https://www.acmicpc.net/problem/2805
"""
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))


# lower_bound
def cut(left, right):
    if left <= right:
        mid = left + (right - left) // 2
        take = sum([t - mid for t in trees if t > mid])
        if take < M:
            return cut(left, mid - 1)
        else:
            return cut(mid + 1, right)
    return right


print(cut(0, max(trees)))
"""
4 7
20 15 10 17
"""