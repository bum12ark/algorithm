"""
출처: https://www.acmicpc.net/problem/1931
"""

size = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(size)]

schedule.sort(key=lambda x: (x[1], x[0]))

result = end = 0
for s, e in schedule:
    if s >= end:
        result += 1
        end = e

print(result)
