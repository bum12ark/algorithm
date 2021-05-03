"""
출처: https://www.acmicpc.net/problem/1260
"""
import collections
import sys
from typing import List

N, M, V = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)


def dfs(v: int, discovered=[]) -> List[int]:
    discovered.append(v)
    for w in sorted(graph[v]):
        if w not in discovered:
            dfs(w, discovered)
    return discovered


def bfs(start_v: int) -> List[int]:
    # 데크 이용
    discovered = [start_v]
    deq = collections.deque([start_v])

    while deq:
        v = deq.popleft()
        for w in sorted(graph[v]):
            if w not in discovered:
                discovered.append(w)
                deq.append(w)
    return discovered


print(*dfs(V))
print(*bfs(V))
