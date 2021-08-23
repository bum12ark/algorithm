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
    # heapq 모듈의 heapify 이용
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 모든 값을 꺼내어 푸시하지 않고도 한 번에 heapify()하여 처리할 수 있다.
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
