"""
* 배열 파티션
n개의 pair를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
- 입력
[1, 4, 3, 2]
- 출력
4
"""
from typing import List


class Solution:
    # 파이썬 다운 풀이
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    solution = Solution()
    param = [1, 4, 3, 2]
    print(solution.arrayPairSum(param))