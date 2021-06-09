"""
출처: https://www.hackerrank.com/challenges/halloween-sale/problem
"""


def halloweenSale(p: int, d: int, m: int, s: int) -> int:
    amount = count = 0
    while amount + p <= s:
        amount += p
        if p - d < m:
            p = m
        else:
            p -= d
        count += 1

    return count


def editorial(p: int, d: int, m: int, s: int) -> int:
    games = 0
    while p <= s:
        s -= p
        p = max(p - d, m)
        games += 1

    return games


if __name__ == '__main__':
    print("===========answer===========")
    print(halloweenSale(20, 3, 6, 85))
    print(editorial(20, 3, 6, 85))
