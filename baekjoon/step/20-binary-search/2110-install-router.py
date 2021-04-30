"""
출처: https://www.acmicpc.net/problem/2110
"""
import sys

N, C = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(N)]


# 거리를 유지하면서 설치할 수 있는 공유기의 숫자
def router_counter(distance: int) -> int:
    cur = x[0]
    count = 1
    for i in range(1, len(x)):
        if cur + distance <= x[i]:
            cur = x[i]
            count += 1
    return count


result = 0


def lower_bound(left: int, right: int) -> int:
    global result
    while left <= right:
        mid = left + (right - left) // 2
        # 설치가능한 라우터가 더 작다면 간격을 더 줄인다.
        if router_counter(mid) < C:
            right = mid - 1
        # 설치가능한 라우터가 더 같거나 많다면 간격을 늘린다.
        else:
            left = mid + 1
            result = max(result, mid)
    return result


x.sort()
print(lower_bound(1, x[-1] - x[0]))
