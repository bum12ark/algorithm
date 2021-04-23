"""
출처: https://www.acmicpc.net/problem/11866
"""
import collections
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

deq = collections.deque(range(1, N + 1))
result = []

print("<", end="")
while deq:
    deq.rotate(-K + 1)
    print(deq.popleft(), end="")
    if deq:
        print(", ", end="")
print(">")
