"""
출처: https://www.acmicpc.net/problem/15652
"""

from typing import List


# 중복 조합
def duplicate_combination(nums: List[int], length: int):
    def dfs(element: List[int], start: int, k: int):
        if k == 0:
            print(' '.join(map(str, element)))
            return

        for i in range(start, len(nums)):
            element.append(nums[i])
            dfs(element, i, k - 1)
            element.pop()

    dfs([], 0, length)


if __name__ == '__main__':
    N, M = map(int, input().split())
    N_list = [x + 1 for x in range(N)]
    duplicate_combination(N_list, M)
