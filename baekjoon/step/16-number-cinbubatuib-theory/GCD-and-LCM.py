"""
출처: https://www.acmicpc.net/problem/2609
"""


def GCD(n, m):
    if n < m:
        n, m = m, n
    if n == 0:
        return m
    if n % m == 0:
        return m
    else:
        return GCD(m, n % m)


def LCM(n, m):
    if n < n:
        n, m = m, n
    return n * m // GCD(n, m)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(GCD(a, b))
    print(LCM(a, b))
