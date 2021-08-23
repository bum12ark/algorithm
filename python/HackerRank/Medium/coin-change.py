"""
출처: https://www.hackerrank.com/challenges/coin-change/problem
"""


def getWay(n, c):
    n_perms = [1] + [0] * n
    for coin in c:
        print("coin", coin)
        for i in range(coin, n + 1):
            print("i", i)
            n_perms[i] += n_perms[i - coin]
    return n_perms


if __name__ == '__main__':
    print("========answer========")
    print(getWay(4, [1, 4, 3]))
