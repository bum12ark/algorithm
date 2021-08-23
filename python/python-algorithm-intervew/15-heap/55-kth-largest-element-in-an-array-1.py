"""
* 배열의 K번째 큰 요소
정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
- Example 1
Input : [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output : 4
"""
import heapq
from typing import List


class Solution:
    # 나의 풀이
    def myFindKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(k):
            result = heapq.heappop(heap)

        return abs(result)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


if __name__ == '__main__':
    print(Solution().myFindKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
