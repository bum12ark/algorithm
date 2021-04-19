"""
출처: https://www.acmicpc.net/problem/5086
"""


def multiple_and_factor(n1: int, n2: int) -> str:
    if n2 % n1 == 0:
        return "factor"
    elif n1 % n2 == 0:
        return "multiple"
    else:
        return "neither"


if __name__ == '__main__':
    while True:
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break

        print(multiple_and_factor(a, b))
