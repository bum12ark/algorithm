"""
url: https://leetcode.com/problems/reconstruct-itinerary/
* 일정 재구성
[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘순으로 방문한다.

- Example 1
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
- Example 2
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)

        route = []

        def DFS(node):
            while graph[node]:
                DFS(graph[node].pop(0))
            route.append(node)

        DFS('JFK')
        return route[::-1]

    def findItinerary_repetition(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


if __name__ == '__main__':
    print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
          "||",
          ["JFK", "MUC", "LHR", "SFO", "SJC"])
    print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]),
          "||",
          ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
    print(Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]),
          "||",
          ["JFK", "NRT", "JFK", "KUL"])

    print(Solution().findItinerary_repetition([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
          "||",
          ["JFK", "MUC", "LHR", "SFO", "SJC"])
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