"""
url: https://leetcode.com/problems/cheapest-flights-within-k-stops/
* K 경유지 내 가장 저렴한 항공권
시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라.
경로가 존재하지 않을 경우 -1을 리턴한다.
- Example 1:
Input:
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 1
Output: 200
"""
import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for f, t, c in flights:
            graph[f].append((t, c))

        Q = [(0, src)]
        count = 0

        while Q:
            _to, _cost = heapq.heappop(Q)


if __name__ == '__main__':
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(Solution().findCheapestPrice(n, edges, src, dst, k), "||", 200)