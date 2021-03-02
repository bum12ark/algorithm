"""
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
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                # 순환 구조이면 False
                if not dfs(y):
                    return False
                # 탐색 종료 후 순환 노드 삭제
                traced.remove((i))

                return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0], [0, 1]]))