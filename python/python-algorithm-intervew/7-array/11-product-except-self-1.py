"""
* 자신을 제외한 배열의 곱
배열을 입력받아 output[i]가 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력하라.
- 입력
input = [1, 2, 3, 4]
- 출력
output = [24, 12, 8, 6]
- 주의
나눗셈을 하지 않고 O(n)에 풀이하라
"""
from typing import List


class Solution:
    # keyword : 왼쪽과 오른쪽에서 자신을 제외한 곱이 없을 때에는 1을 대입해준다.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 자신을 제외한 왼쪽 곱셈의 값
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        # 자신을 제외한 오른쪽 곱셈의 값
        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] *= p
            p *= nums[i]
        return out


if __name__ == '__main__':
    solution = Solution()
    param = [1, 2, 3, 4]
    print(solution.productExceptSelf(param))
