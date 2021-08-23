"""
출처: https://www.acmicpc.net/problem/15651
"""


# 중복 순열
def duplicate_permutation(nums, length):
    def dfs(element, k):
        if k == 0:
            print(' '.join(map(str, element)))
            return

        for n in nums:
            element.append(n)
            dfs(element, k - 1)
            element.pop()

    dfs([], length)


if __name__ == '__main__':
    N, M = map(int, input().split())
    N_list = [x + 1 for x in range(N)]
    duplicate_permutation(N_list, M)
