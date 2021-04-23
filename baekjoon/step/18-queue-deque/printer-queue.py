"""
출처: https://www.acmicpc.net/problem/1966
"""
import collections
import sys

test_case = int(sys.stdin.readline().rstrip())
for _ in range(test_case):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    importance = list(map(int, sys.stdin.readline().rstrip().split()))

    # (중요도, 인덱스)
    item = [(val, idx) for idx, val in enumerate(importance)]
    count = 0
    deq = collections.deque(item)

    while deq:
        max_importance = max(deq)[0]
        p, i = deq.popleft()
        if p == max_importance:
            count += 1
            if i == M:
                print(count)
                break
        else:
            deq.append((p, i))
