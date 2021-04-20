"""
출처: https://www.acmicpc.net/problem/1934
"""


def gcb(n, m):
    if n < m:
        n, m = m, n
    if n == 0:
        return m
    if n % m == 0:
        return m
    return gcb(m, n % m)


def lcm(n, m):
    if n < m:
        n, m = m, n
    return n * m // gcb(n, m)


if __name__ == '__main__':
    size = int(input())
    for _ in range(size):
        a, b = map(int, input().split())
        print(lcm(a, b))
