"""
* 일정 재구성
[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘순으로 방문한다.
- Example 1
Input : [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output : ["JFK", "MUC", "LHR", "SFO", "SJC"]
- Exmaple 2
Input : [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
Output : ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
"""
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프화 시키기 map[List[str]]
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        result = []
        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            result.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return result[::-1]

if __name__ == '__main__':
    solution = Solution()
    param1 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(solution.findItinerary(param1))
