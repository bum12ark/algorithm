"""
출처: https://www.acmicpc.net/problem/11286
"""
import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(command), command))
