"""
출처: https://www.acmicpc.net/problem/18258
"""
import collections
import sys

size = int(sys.stdin.readline().rstrip())
item = collections.deque()
for _ in range(size):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        item.append(command[1])
    elif command[0] == "pop":
        print(item.popleft()) if item else print(-1)
    elif command[0] == "size":
        print(len(item))
    elif command[0] == "empty":
        print(1) if not item else print(0)
    elif command[0] == "front":
        print(item[0]) if item else print(-1)
    elif command[0] == "back":
        print(item[len(item) - 1]) if item else print(-1)
