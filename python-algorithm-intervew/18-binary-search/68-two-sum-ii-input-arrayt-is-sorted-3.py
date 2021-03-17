"""
* 두수의 합 II
정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
주의 : 이 문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
"""
import bisect
from typing import List


class Solution:
    # bisect 모듈 + 슬라이싱
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, v in enumerate(numbers):
            expected = target - v
            k = bisect.bisect_left(numbers[i + 1:], expected)
            if k < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
                return i + 1, i + k + 2


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))