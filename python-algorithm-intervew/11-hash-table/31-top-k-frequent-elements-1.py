"""
* 상위 K 빈도 요소
상위(많이 등장하는 순서대로) k번 이상 등장하는 요소를 추출하라.
- Example 1
Input : nums = [1, 1, 1, 2, 2, 3], k = 2
Output : [1, 2]
"""
import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        print(freqs_heap)

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 2, 2, 3], 2))