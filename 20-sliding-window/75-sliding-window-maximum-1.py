"""
* 최대 슬라이딩 윈도우
배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.
- Example
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))

        return result

if __name__ == '__main__':
    param = [1, 3, -1, -3, 5, 3, 6, 7]
    print(Solution().maxSlidingWindow(param, 3))