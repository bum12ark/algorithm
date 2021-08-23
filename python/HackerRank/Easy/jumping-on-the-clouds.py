"""
출처: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""
from typing import List


def jumpingOnClouds(c: List[int]) -> int:
    current = answer = 0
    while current < len(c) - 1:
        next = current + 2
        if len(c) - 1 < next:
            next = len(c) - 1

        if c[next] != 1:
            current += 2
        else:
            current += 1
        answer += 1

    return answer


def editorial(c: List[int]) -> int:
    current = answer = 0
    while current < len(c) - 1:
        if current + 2 >= len(c) or c[current + 2] == 1:  # Not possible to make a jump to size 2
            current += 1
        else:
            current += 2

        answer += 1

    return answer


if __name__ == '__main__':
    print("=======answer=======")
    p1 = [0, 0, 0, 1, 0, 0]
    print(jumpingOnClouds(p1))
    print(editorial(p1))
