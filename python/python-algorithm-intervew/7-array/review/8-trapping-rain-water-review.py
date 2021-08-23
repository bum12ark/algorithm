"""
url: https://leetcode.com/problems/trapping-rain-water/
* 빗물 트래핑
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓을 수 있는지 계산하라.

- Example
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        volume = 0

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


if __name__ == '__main__':
    height_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height_1), '||', '6')
"""
[시작 체크 리스트]
[✓] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""