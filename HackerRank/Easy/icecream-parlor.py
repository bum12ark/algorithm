"""
출처: https://www.hackerrank.com/challenges/icecream-parlor/problem
"""


def icecreamParlor(m, arr):
    nums_map = {}
    for i, n in enumerate(arr):
        if m - n in nums_map:
            return [nums_map[m - n], i + 1]
        #  value: index 저장
        nums_map[n] = i + 1


print(icecreamParlor(5, [1, 3, 4, 5, 6]))
