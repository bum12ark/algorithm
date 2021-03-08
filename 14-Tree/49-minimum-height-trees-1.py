"""
* 최소 높이 트리
노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라.
- Example 1
Input : n = 4, edges = [[1, 0], [1, 2], [1, 3]]
   0
   |
   1
 /  \
2   3
Output : [1]
- Example 2
Input : n = 6, edge = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
0  1  2
\  |  /
   3
   |
   4
   |
   5
Output : [3, 4]
Explanation : 3 또는 4가 루트가 되는 트리가 될 경우 최대 높이 2인 트리가 된다.
"""
import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향으로 삽입하여 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 (그래프에서 해당 키의 값이 1개뿐인 것)
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때 까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neigbor = graph[leaf].pop()
                graph[neigbor].remove(leaf)

                if len(graph[neigbor]) == 1:
                    new_leaves.append(neigbor)
            leaves = new_leaves

        return leaves


if __name__ == '__main__':
    param1 = 10
    param2 = [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]
    print(Solution().findMinHeightTrees(param1, param2))