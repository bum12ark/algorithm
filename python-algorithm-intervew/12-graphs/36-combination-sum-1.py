"""
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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[str]]:
        result = []
        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 5], 8))