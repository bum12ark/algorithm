"""
출처: https://www.acmicpc.net/problem/9375
"""
import collections
import sys
from typing import Dict, List


def dressed(p_map: Dict[str, List[str]]) -> int:
    # 파라미터 체크
    if not p_map:
        return 0

    result = 1
    # (의상의 종류의 숫자 + 아무것도 입지 않는 경우) 중 하나를 고르는 조합 (n + 1 Combination 1)
    for key in p_map:
        result *= len(p_map[key]) + 1

    return result - 1  # 의상을 모두 아무것도 입지 않는 한가지 경우를 빼준다.


if __name__ == '__main__':
    T = int(sys.stdin.readline())  # 테스트 케이스의 개수

    for _ in range(T):
        N = int(sys.stdin.readline())  # 의상의 개수
        dic = collections.defaultdict(list)  # 의상의 종류와 이름을 담을 딕셔너리
        for _ in range(N):
            clothes, kind = sys.stdin.readline().split()
            dic[kind].append(clothes)

        answer = dressed(dic)
        print(answer)
