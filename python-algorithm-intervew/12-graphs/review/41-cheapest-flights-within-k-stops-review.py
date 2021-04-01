"""
url: https://leetcode.com/problems/cheapest-flights-within-k-stops/
* K 경유지 내 가장 저렴한 항공권
시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라.
경로가 존재하지 않을 경우 -1을 리턴한다.
- Example 1:
Input:
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 0
Output: 500
"""
import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for f, t, w in flights:
            graph[f].append((t, w))

        # 가격, 정점, 소요시간
        Q = [(0, src, K)]

        # 우선 순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while Q:
            _price, _node, _k = heapq.heappop(Q)
            if _node == dst:
                return _price
            if _k >= 0:
                for v, w in graph[_node]:
                    alt = w + _price
                    heapq.heappush(Q, (alt, v, _k - 1))

        return -1



if __name__ == '__main__':
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(Solution().findCheapestPrice(n, edges, src, dst, k), "||", 200)
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