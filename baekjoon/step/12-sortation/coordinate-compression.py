"""
출처: https://www.acmicpc.net/problem/18870
"""
import heapq

if __name__ == '__main__':
    size = int(input())
    nums = list(map(int, input().split()))
    heap = []
    for n in set(nums):
        heapq.heappush(heap, n)
    print(heap)
    count = 0
    while heap:
        num = heapq.heappop(heap)
