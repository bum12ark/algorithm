"""
url: https://leetcode.com/problems/combinations/
* 조합
전체 수 n을 입력받아 k개의 조합을 리턴하라
- Example 1
Input: n = 4, k = 2
Output: [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
- Example 2
Input: n = 1, k = 1
Output: [[1]]
"""
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def DFS(element, start, k):
            if k == 0:
                result.append(element.copy())
                return

            for idx in range(start, n + 1):
                element.append(idx)
                DFS(element, idx + 1, k - 1)
                element.pop()

        DFS([], 1, k)
        return result

    def combine_itertools(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


if __name__ == '__main__':
    print(Solution().combine(4, 2), "||", [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])
    print(Solution().combine_itertools(4, 2), "||", [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[✓] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""
