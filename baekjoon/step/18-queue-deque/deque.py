"""
출처: https://www.acmicpc.net/problem/10866
"""
import collections
import sys

size = int(sys.stdin.readline().rstrip())
item = collections.deque()
for _ in range(size):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push_front":
        item.appendleft(command[1])
    elif command[0] == "push_back":
        item.append(command[1])
    elif command[0] == "pop_front":
        print(item.popleft()) if item else print(-1)
    elif command[0] == "pop_back":
        print(item.pop()) if item else print(-1)
    elif command[0] == "size":
        print(len(item))
    elif command[0] == "empty":
        print(1) if not item else print(0)
    elif command[0] == "front":
        print(item[0]) if item else print(-1)
    elif command[0] == "back":
        print(item[len(item) - 1]) if item else print(-1)
