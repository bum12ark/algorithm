"""
출처: https://www.acmicpc.net/problem/5430
"""
import collections
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    x = list(sys.stdin.readline().rstrip()[1:-1].split(','))

    if n == 0:
        x = []
    deque = collections.deque(x)
    left = True
    try:
        for command in p:
            if command == "R":
                left = not left
            elif command == "D":
                if left:
                    deque.popleft()
                else:
                    deque.pop()
        print("["+",".join(deque)+"]") if left else print("["+",".join(reversed(deque))+"]")
    except IndexError:
        print("error")

