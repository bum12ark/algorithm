"""
출처: https://www.acmicpc.net/problem/2164
"""
import collections
import sys

N = int(sys.stdin.readline())
deq = collections.deque(range(1, N + 1))

while len(deq) > 1:
    # 제일 위에 있는 카드를 바닥에 버린다.
    deq.popleft()
    # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    deq.rotate(-1)

print(deq.pop())
