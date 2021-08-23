"""
출처: https://www.hackerrank.com/challenges/plus-minus/problem
"""


def plusMinus(arr):
    n = len(arr)
    positive = negative = zeros = 0
    for num in arr:
        if num < 0:
            negative += 1
        elif num > 0:
            positive += 1
        else:
            zeros += 1

    print("{:.6f}".format(positive / n))
    print("{:.6f}".format(negative / n))
    print("{:.6f}".format(zeros / n))


plusMinus([-4, 3, -9, 0, 4, 1])
