"""
* 키에 따른 대기열 재구성
여러 명의 사람들이 줄을 서 있다. 각각의 사람은 (h, k)의 두 정수 쌍을 갖는데,
h는 그 사람의 키, k는 앞에 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수를 뜻한다.
이 값이 올바르도록 줄을 재정렬하는 알고리즘을 작성하라.
- Example
Input: [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
Output: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
"""
import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for h, k in people:
            heapq.heappush(heap, (-h, k))

        result = []
        while heap:
            h, k = heapq.heappop(heap)
            result.insert(k, [-h, k])

        return result


if __name__ == '__main__':
    param = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(param))
