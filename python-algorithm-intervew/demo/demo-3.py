import collections


def solution(P, S):
    preson = sum(P)
    count = 0
    for n in sorted(S, reverse=True):
        remain = preson - n
        if remain > 0:
            preson = remain
            count += 1
        if remain == 0:
            count += 1
            break
    return count

print(solution([1, 4, 1], [1, 5, 1]))