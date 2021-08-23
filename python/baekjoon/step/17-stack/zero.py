"""
출처: https://www.acmicpc.net/problem/10773
"""
import sys

size = int(sys.stdin.readline())

stack = []
for _ in range(size):
    n = int(sys.stdin.readline().rstrip())
    if n == 0 and stack:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
