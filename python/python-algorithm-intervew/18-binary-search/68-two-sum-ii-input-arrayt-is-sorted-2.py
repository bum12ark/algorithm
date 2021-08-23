"""
* 두수의 합 II
정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
주의 : 이 문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
"""
from typing import List


class Solution:
    # 현재 값을 기준으로 나머지 값이 맞는지 확인하는 형태의 이진 검색 풀이
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            expected = target - n
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return i + 1, mid + 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
