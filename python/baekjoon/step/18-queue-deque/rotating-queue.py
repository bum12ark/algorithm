"""
출처: https://www.acmicpc.net/problem/1021
"""
import collections
import sys


N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))

nums = range(1, N + 1)
deque = collections.deque(nums)
count = 0

while M:
    for val in targets:
        d_index = deque.index(val)
        d_len = len(deque)
        if d_index <= d_len // 2:
            deque.rotate(-d_index)
            count += d_index
        else:
            deque.rotate(d_len - d_index)
            count += d_len - d_index
        deque.popleft()
        M -= 1

print(count)
