"""
* 세수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

- 입력
nums = [-1, 0, 1, 2, -1, -4]
- 출력
[
    [-1, 0, 1],
    [-1, -1, 2]
]

"""
from typing import List


class Solution:
    # 투 포인터로 합 계산
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # 포인터를 사용하기 위해 정렬

        for i in range(len(nums) - 2):
            # 중복 값 건너 뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 중복 값 건너 뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

if __name__ == '__main__':
    solution = Solution()
    param:List[str] = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(param))
