"""
출처: https://www.acmicpc.net/problem/15650
"""
from typing import List


def combination(nums: List[int], length: int):
    def dfs(element: List[int], start: int, k: int):
        # 탈출
        if k == 0:
            print(' '.join(map(str, element)))
            return

        for i in range(start, len(nums)):
            element.append(nums[i])
            # 현재 인덱스 다음 인덱스 부터 순회
            dfs(element, i + 1, k - 1)
            element.pop()

    dfs([], 0, length)


if __name__ == '__main__':
    N, M = map(int, input().split())
    N_list = [x + 1 for x in range(N)]
    combination(N_list, M)
