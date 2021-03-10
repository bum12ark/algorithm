"""
* 배열의 K번째 큰 요소
정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
- Example 1
Input : [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output : 4
"""
from typing import List


# 정렬을 이용한 풀이
class Solution:
    # 나의 풀이
    def myFindKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]



if __name__ == '__main__':
    print(Solution().myFindKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))