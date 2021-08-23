"""
출처: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""
#!/bin/python3
import bisect
import collections
import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    answer = []
    ranked = sorted(set(ranked))

    for score in player:
        answer.append(len(ranked) - bisect.bisect_right(ranked, score) + 1)

    return answer


if __name__ == '__main__':
    fptr = sys.stdin

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
