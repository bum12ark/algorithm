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
    # 짝수번째 값 풀이 (오름차순 정렬을 하였을 때 0, 2, 4, ... 인덱스 값이 최솟값인 점을 활용)
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum


if __name__ == '__main__':
    solution = Solution()
    param = [1, 4, 3, 2]
    print(solution.arrayPairSum(param))