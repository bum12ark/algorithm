"""
url: https://leetcode.com/problems/3sum/
* 세수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

- Example :
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""
from typing import List


class Solution:
    # 정렬해서 투포인터로 풀면 될꺼 같아
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for idx in range(len(nums) - 2):
            left = idx + 1
            right = len(nums) - 1

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            while left < right:
                _sum = nums[left] + nums[right] + nums[idx]
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    result.append([nums[idx], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    print(Solution().threeSum([0, 0, 0]), [0])
    print(Solution().threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
    print(Solution().threeSum([-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]),
          [[-5, 1, 4], [-3, -1, 4], [-3, 0, 3], [-2, -1, 3], [-2, 1, 1], [-1, 0, 1], [0, 0, 0]])
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