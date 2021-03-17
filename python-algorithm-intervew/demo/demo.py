import collections
from typing import List


def solution(A: List[int]):
    # 배열이 존재하지 않을 경우 0 반환
    if not A:
        return 0

    one_digit = 0
    for n in A:
        if 0 <= n < 10:
            one_digit = max(one_digit, n)

    return one_digit

print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))