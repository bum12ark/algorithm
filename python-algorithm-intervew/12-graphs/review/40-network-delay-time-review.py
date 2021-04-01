"""
url: https://leetcode.com/problems/network-delay-time/
* 네트워크 딜레이 타임
K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다.
입력값 (u, v, w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

- Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
- Example2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
"""
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for f, t, c in times:
            graph[f].append((t, c))
        print(graph)

        # 소요시간, 노드
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            _cost, _from = heapq.heappop(Q)
            if _from not in dist:
                dist[_from] = _cost
                for v, w in graph[_from]:
                    alt = _cost + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == n:
            return max(dist.values())

        return -1


if __name__ == '__main__':
    print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), "||", 2)
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[✓] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""