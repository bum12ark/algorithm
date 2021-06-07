"""
출처: https://www.hackerrank.com/challenges/between-two-sets/problem
"""
import math


# 두 수 이상의 최대공약수는 두 수의 최대공약수와 나머지 한 수의 최대공약수가 세 수 의 최대 공약수가 된다.
def gcd_list(arr):
    if len(arr) == 1:
        return arr[0]

    result = arr[0]
    for i in range(1, len(arr)):
        result = math.gcd(result, arr[i])

    return result


def lmc_list(arr):
    def lcm(a, b):  # 최소 공배수
        return int(a * b / math.gcd(a, b))

    if len(arr) == 1:
        return arr[0]

    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])

    return result


# a의 배수인 동시에 b의 약수인 정수의 개수
def getTotalX(a, b):
    lmc_a = lmc_list(a)
    print(lmc_a)
    gcd_b = gcd_list(b)
    print(gcd_b)

    answer = 0
    while lmc_a <= gcd_b:
        if lmc_a % gcd_b == 0:
            answer += 1


getTotalX([2, 4], [16, 32, 96])
