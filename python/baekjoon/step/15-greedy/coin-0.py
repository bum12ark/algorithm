"""
출처: https://www.acmicpc.net/problem/11047
"""


def zero_coin(coin, value):
    result = 0
    for i in range(len(coin) - 1, -1, -1):
        if coin[i] > value:
            continue
        # 몫을 추가
        result += value // coin[i]
        # 나머지 값으로 초기화
        value %= coin[i]
    return result


if __name__ == '__main__':
    size, value = map(int, input().split())
    coin = [int(input()) for _ in range(size)]
    print(zero_coin(coin, value))
