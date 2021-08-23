"""
출처: https://www.acmicpc.net/problem/11050
"""
import sys


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


if __name__ == '__main__':
    n, r = map(int, sys.stdin.readline().rstrip().split())
    print(combination(n, r))
