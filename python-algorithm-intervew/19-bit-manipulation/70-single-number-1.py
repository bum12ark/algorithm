"""
* 싱글 넘버
딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라.
- Example 1
Input: [2, 2, 1]
Output: 1
- Example 2
Input: [4, 1, 2, 1, 2]
Output: 4
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result


if __name__ == '__main__':
    param = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(param))