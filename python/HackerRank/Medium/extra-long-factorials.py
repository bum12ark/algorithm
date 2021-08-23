"""
출처: https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""
#!/bin/python3
import collections
import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

dp = collections.defaultdict(int)

def extraLongFactorials(n):
    # Write your code here
    if n in dp:
        return dp[n]

    if n <= 1:
        return 1

    dp[n] = n * extraLongFactorials(n - 1)
    return dp[n]

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
