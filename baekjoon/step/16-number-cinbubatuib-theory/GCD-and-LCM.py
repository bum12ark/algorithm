"""
출처: https://www.acmicpc.net/problem/2609
"""

def eclidean_GCD(n, m):
    if n < m:
        n, m = m, n
    if n == 0:
        return m
    if n % m == 0:
        return m
    else:
        return eclidean_GCD(m, n % m)
