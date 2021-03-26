"""
url: https://leetcode.com/problems/product-of-array-except-self/
* 자신을 제외한 배열의 곱
배열을 입력받아 output[i]가 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력하라.

- Example
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Caution: 나눗셈을 하지 않고 O(n)에 풀이하라
"""
from typing import List


class Solution:
    # 왼쪽 곱셈에서 오른쪽 곱셈 더하기
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for value in nums:
            out.append(p)
            p *= value

        p = 1
        for idx in range(len(nums) - 1, -1, -1):
            out[idx] *= p
            p *= nums[idx]

        return out


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8 , 6])
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[✓] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""