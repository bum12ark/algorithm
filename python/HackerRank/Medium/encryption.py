"""
출처: https://www.hackerrank.com/challenges/encryption/problem
"""
import collections
import math

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")  # 공백제거
    length = len(s)
    L = math.sqrt(length)
    row = math.floor(L)
    col = math.ceil(L)

    while row * col < length:  # validation
        if row < col:
            row += 1
        else:
            col += 1

    answer = []
    for i in range(col):
        answer.append(s[i::col] + " ")

    return "".join(answer)


if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
