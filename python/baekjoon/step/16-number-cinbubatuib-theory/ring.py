"""
출처: https://www.acmicpc.net/problem/3036
"""


def gcd(n, m):
    if n < m:
        n, m = m, n
    if m == 0:
        return m
    if n % m == 0:
        return m
    return gcd(m, n % m)


if __name__ == '__main__':
    size = int(input())
    nums = list(map(int, input().split()))
    for i in range(1, size):
        g = gcd(nums[0], nums[i])
        print("{0}/{1}".format(nums[0] // g, nums[i] // g))