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
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass


if __name__ == '__main__':
    print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
          "||",
          ["JFK", "MUC", "LHR", "SFO", "SJC"])
