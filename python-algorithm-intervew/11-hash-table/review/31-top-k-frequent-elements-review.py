"""
* 상위 K 빈도 요소
상위(많이 등장하는 순서대로) k번 이상 등장하는 요소를 추출하라.

- Example 1
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
- Example 2
Input: nums = [1], k = 1
Output: [1]
"""
import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)

        heap = []
        for val in counts:
            heapq.heappush(heap, (-counts[val], val))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2), "||", [1, 2])
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[✓] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""