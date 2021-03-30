"""
url: https://leetcode.com/problems/combination-sum/
* 조합의 합
숫자 집합 candidate를 조합하여 합이 target이 되는 원소를 나열하라.
각 원소는 중복으로 나열 가능하다.
- Example 1
Input : candidates = [2, 3, 6, 7], target = 7
Output : [
    [7],
    [2, 2, 3]
]
- Example 2
Input : candidates = [2, 3, 5], target = 8
Output : [
    [2, 2, 2, 2],
    [2, 3, 3,],
    [3, 5]
]
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def DFS(csum, start, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for idx in range(start, len(candidates)):
                DFS(csum - candidates[idx], idx, path + [candidates[idx]])

        DFS(target, 0, [])
        return result


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7), "||", [[7], [2, 2, 3]])
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