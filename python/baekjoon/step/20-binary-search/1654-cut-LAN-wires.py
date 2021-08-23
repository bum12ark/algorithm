"""
출처: https://www.acmicpc.net/problem/1654
"""
import sys

K, N = map(int, sys.stdin.readline().split())
wires = [int(sys.stdin.readline()) for _ in range(K)]
result = 0


def cut_recursive(left, right):
    if left <= right:
        mid = left + (right - left) // 2
        cnt = sum([w // mid for w in wires])
        if cnt < N:
            # 범위 줄이기
            return cut_recursive(left, mid - 1)
        elif cnt >= N:
            # 범위 늘리기
            return cut_recursive(mid + 1, right)
    # 제일 자를 수 있는 마지막 값
    return right


def cut_loop(left, right):
    while left <= right:
        mid = left + (right - left) // 2
        cnt = sum([w // mid for w in wires])
        if cnt < N:
            right = mid - 1
        else:
            left = mid + 1
    return right


def lower_bound(left, right):
    global result
    while left <= right:
        mid = left + (right - left) // 2
        cnt = sum([w // mid for w in wires])
        # 만약 자를 수 있는 랜선의 합이, 적어도 가져가야 하는 값보다 작으면 길이를 낮게설정
        # - 가져갈 수 있는 선을 많게 한다.
        if cnt < N:
            right = mid - 1
        else:
            left = mid + 1
            result = max(result, mid)
    return result


# 1부터 가장 큰 수까지 자르기
# print(cut_recursive(1, max(wires)))
# print(cut_loop(1, max(wires)))
print(lower_bound(1, max(wires)))

"""
4 3
1
2
3
3
"""
