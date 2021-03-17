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
    # heapq 모듈의 nlargest 이용
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq 모듈 중 n번 째 큰 값을 추출하는 기능도 제공한다.
        # k번째만큼 큰 값이 가장 큰 값 부터 순서대로 리스트로 리턴된다. -> [6, 5, 5, 4]
        # 여기서 마지막 인덱스 -1이 k번째 값이 된다.
        # 내부적으로 heapify() 함수도 호출해 처리해주기 때문에, 별도의 힙 처리를 할 필요가 없다.
        # nsmallest()를 사용하면 동일한 방식으로 n번째 작은 값도 추출이 가능하다.
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
