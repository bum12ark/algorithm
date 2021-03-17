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
    # 브루트 포스 방식으로 풀이 (n^3)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        return result



if __name__ == '__main__':
    solution = Solution()
    param:List[str] = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(param))