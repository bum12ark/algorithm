"""
* 원점에 K번째로 가까운 점
평면상에 points 목록이 있을 때, 원점 (0, 0)에서 K번 가까운 점 목록을 순서대로 출력하라.
평면상 두 점의 거리는 유클리드 거리로 한다.
- Example 1
Input: points = [[1, 3], [-2, 2]], K = 1
Output: [[-2, 2]]
Explanation: (1, 3)과의 거리는 루트 10이고 (-2, 2)와의 거리는 루트 8이다.
             두 번째가 더 가까우며, K = 1로 가장 가까운 거리 K는 [[-2, 2]] 이다.
- Example 2
Input: points = [[3, 3], [5, -1], [-2, 4]], K = 2
Output: [[3, 3], [-2, 4]]
Explanation: 가장 가까운 거리 K=2 개는 [[3, 3], [-2, 4]] 이다.
"""
import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            # 유클리드 거리 구하기
            dist = math.sqrt((0 - x) ** 2 + (0 -y) ** 2)
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))

        return result


if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    K = 1
    print(Solution().kClosest(points, K))