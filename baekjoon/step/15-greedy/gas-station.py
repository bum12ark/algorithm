"""
출처: https://www.acmicpc.net/problem/13305
"""
import sys

size = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
min_price = sys.maxsize
for i in range(len(price) - 1):
    # 가장 작은 값으로 초기화
    min_price = min(price[i], min_price)
    result += min_price * distance[i]

print(result)
