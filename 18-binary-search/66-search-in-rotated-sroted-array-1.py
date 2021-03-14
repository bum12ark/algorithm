"""
* 회전 정렬된 배열 검색 (복습)
특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라.
Input: nums = [4, 5, 6, 7, 0, 1], target = 1
Output: 5
Explanation: 정렬된 입력값은 [0, 1, 2, 4, 5, 6, 7]이며 여기서 이진 검색을 통해
             1의 위치를 찾은 다음 (위치1) 원래의 입력값에서 얼마만큼 돌아가 있는지를 확인하여(4칸),
             '위치 1 + 4칸 = 인덱스 5'를 리턴한다.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass
    
if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1], 1))