"""
출처: https://www.acmicpc.net/problem/9184
"""

MAX = 21
dp = [
    [
        [0] * MAX for _ in range(MAX)
    ] for _ in range(MAX)
]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return dp[a][b][c]


if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().split())

        if a == -1 and b == -1 and c == -1:
            break

        print("w({0}, {1}, {2}) = {3}".format(a, b, c, w(a, b, c)))
