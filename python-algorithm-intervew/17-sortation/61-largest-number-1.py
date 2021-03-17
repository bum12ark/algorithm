"""
* 가장 큰 수
항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.
- Example 1
Input: [10, 2]
Output: 210
- Example 2
Input: [3, 30, 34, 5, 9]
Output: 9534330
"""
from typing import List


class Solution:
    def to_swap(self, n1, n2) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        i: int = 1
        while i < len(nums):
            j: int = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j = j - 1
            i = i + 1
        dist = map(str, nums)

        return str(int(''.join(map(str, nums))))


if __name__ == '__main__':
    param1 = [0, 0]
    param2 = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(param1))