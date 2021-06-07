"""
출처: https://www.hackerrank.com/challenges/between-two-sets/problem
"""
import math


from typing import List


# 두 수 이상의 최대공약수는 두 수의 최대공약수와 나머지 한 수의 최대공약수가 세 수 의 최대 공약수가 된다.
def gcd_list(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]

    result = arr[0]
    for i in range(1, len(arr)):
        result = math.gcd(result, arr[i])

    return result


def lmc_list(arr: List[int]) -> int:
    def lcm(a: int, b: int) -> int:  # 최소 공배수
        return int(a * b / math.gcd(a, b))

    if len(arr) == 1:
        return arr[0]

    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])

    return result


# a의 배수인 동시에 b의 약수인 정수의 개수
def getTotalX(a: int, b: int) -> int:
    multiple = lmc_a = lmc_list(a)
    gcd_b = gcd_list(b)

    answer = 0
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            answer += 1
        multiple += lmc_a
    return answer


print(getTotalX([1], [100]))
