"""
출처: https://www.acmicpc.net/problem/2606
"""
import collections
import sys


N = int(sys.stdin.readline())
computers = int(sys.stdin.readline())
network = collections.defaultdict(list)

for _ in range(computers):
    s, e = map(int, sys.stdin.readline().split())
    network[s].append(e)
    network[e].append(s)


def dfs(v, discovered=[]):
    discovered.append(v)
    for w in network[v]:
        if w not in discovered:
            dfs(w)
    return discovered


def bfs(start_v):
    discovered = [start_v]
    deq = collections.deque([start_v])
    while deq:
        v = deq.popleft()
        for w in network[v]:
            if w not in discovered:
                discovered.append(w)
                deq.append(w)
    return discovered


print(len(dfs(1)) - 1)

