"""
url: https://leetcode.com/problems/array-partition-i/
* 배열 파티션
n개의 pair를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

- Example
Input: nums = [1,4,3,2]
Output: 4
"""
from typing import List


class Solution:
    # 짝수 번째 값 더하기 - 슬라이싱 사용
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    print(Solution().arrayPairSum([1, 4, 3, 2]), 4)
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[✓] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""