"""
출처: https://www.acmicpc.net/problem/14889
"""
import itertools
import sys


def calculate_ability(table, n):
    possible_team = list(itertools.combinations([x + 1 for x in range(n)], n // 2))
    result = sys.maxsize
    for idx in range(len(possible_team) // 2):
        team_a = possible_team[idx]
        team_b = possible_team[len(possible_team) - idx - 1]

        ability_a = 0
        for x, y in list(itertools.permutations(team_a, 2)):
            # 인덱스에 맞추기 위해 -1
            ability_a += table[x - 1][y - 1]

        ability_b = 0
        for x, y in list(itertools.permutations(team_b, 2)):
            ability_b += table[x - 1][y - 1]

        result = min(result, abs(ability_a - ability_b))

    return result


if __name__ == '__main__':
    size = int(input())
    t = [list(map(int, input().split())) for _ in range(size)]

    print(calculate_ability(t, size))