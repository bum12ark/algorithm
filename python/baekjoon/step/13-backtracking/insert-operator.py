"""
출처: https://www.acmicpc.net/problem/14888
"""
import sys


def dfs(num, idx, plus, minus, multiple, division):
    global size, max_value, min_value
    if idx == size:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return
    else:
        if plus:
            dfs(num + nums[idx], idx + 1, plus - 1, minus, multiple, division)
        if minus:
            dfs(num - nums[idx], idx + 1, plus, minus - 1, multiple, division)
        if multiple:
            dfs(num * nums[idx], idx + 1, plus, minus, multiple - 1, division)
        if division:
            dfs(int(num / nums[idx]), idx + 1, plus, minus, multiple, division - 1)


if __name__ == '__main__':
    max_value = -sys.maxsize
    min_value = sys.maxsize

    size = int(input())
    nums = list(map(int, input().split()))
    pl, mi, mu, di = map(int, input().split())

    dfs(nums[0], 1, pl, mi, mu, di)

    print(max_value)
    print(min_value)
