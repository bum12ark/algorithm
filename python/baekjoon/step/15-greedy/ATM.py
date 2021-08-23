"""
출처: https://www.acmicpc.net/problem/11399
"""

# param
size = int(input())
p_times = list(map(int, input().split()))

# solution
p_times.sort()
prev = result = 0
for t in p_times:
    prev += t
    result += prev

# result
print(result)
