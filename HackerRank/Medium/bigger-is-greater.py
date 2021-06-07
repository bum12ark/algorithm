"""
출처: https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""


def biggerIsGreater(w):
    arr = list(w)

    # 증가하지 않는 접미사 찾기
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"

    # 피벗 후계자 찾기
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[j], arr[i - 1] = arr[i - 1], arr[j]

    # Reverse
    arr[i:] = arr[len(arr) - 1: i - 1: -1]

    return "".join(arr)
