"""
url: https://leetcode.com/problems/course-schedule/
* 코스 스케줄
0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍으로 표현하는 n개의 코스가 있다.
코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.
- Example 1
Input : 2 [[1, 0]]
Output : true
Explanation : 2개의 코스가 있으며, 1을 완료하기 위해 0을 끝내면 된다. 따라서 가능하다.
- Example 2
Input : 2, [[1, 0], [0, 1]]
Output: false
Explanation : 2개의 코스가 있으며, 1을 완료하기 위해서는 0을 끝내야 하고,
0을 완료하기 위해서는 1을 끝내야한다. 따라서 불가능하다.
"""
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for _from, _to in prerequisites:
            graph[_from].append(_to)

        traced = set()

        def DFS(node):
            if node in traced:
                return False

            traced.add(node)
            for n in graph[node]:
                if not DFS(n):
                    return False
            traced.remove(node)

            return True

        for i in list(graph):
            if not DFS(i):
                return False

        return True

    def canFinish_optimization(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for _from, _to in prerequisites:
            graph[_from].append(_to)

        traced = set()
        visited = set()

        def DFS(node):
            # 순환구조이면 False
            if node in traced:
                return False
            # 이미 방문했던 노드이면 True
            if node in visited:
                return True

            traced.add(node)
            for n in graph[node]:
                if not DFS(n):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(node)
            # 탐색 종료 후 방문 노드 추가
            visited.add(node)

        # 순환 구조 판별
        for x in list(graph):
            if not DFS(x):
                return False

        return True



if __name__ == '__main__':
    print(Solution().canFinish(3, [[0, 1], [0, 2], [1, 2]]), "||", True)
    # print(Solution().canFinish(2, [[0, 1], [1, 0]]), "||", False)
"""
[시작 체크 리스트]
[✓] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""