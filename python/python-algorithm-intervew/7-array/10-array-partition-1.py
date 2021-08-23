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
    # 오름차순 풀이
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair.clear() # 페어 초기화

        return sum


if __name__ == '__main__':
    solution = Solution()
    param = [1, 4, 3, 2]
    print(solution.arrayPairSum(param))