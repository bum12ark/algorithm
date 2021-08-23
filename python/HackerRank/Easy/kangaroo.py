"""
출처: https://www.hackerrank.com/challenges/kangaroo/problem
"""


def kangaroo(x1, v1, x2, v2):
    # x1 < x2 제약 조건 으로 인하여 속도가 같거나 느리면 만날 수 없다.
    if v1 <= v2:
        return "NO"

    while True:
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"

        if x1 > x2:
            return "NO"
