"""
* 위장

"""
import collections


def solution(clothes):
    dist = collections.defaultdict(list)

    for name, kind in clothes:
        dist[kind].append(name)

    result = 1
    for key in dist.keys():
        result = result * (len(dist[key]) + 1)

    return result - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))