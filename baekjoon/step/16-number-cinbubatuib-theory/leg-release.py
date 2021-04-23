"""
출처: https://www.acmicpc.net/problem/1010
"""
import sys
from math import factorial

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))
