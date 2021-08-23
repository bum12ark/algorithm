"""
출처: https://www.hackerrank.com/challenges/countingsort4/problem
"""
from typing import List


def countSort(arr: List[List[str]]) -> None:
    lst = []
    # 처음부터 절반까지 '-'로 치환, 정렬을 위해 int 형으로 변환
    for i in range(len(arr)):
        if i < len(arr) // 2:
            lst.append((int(arr[i][0]), '-'))
        else:
            lst.append((int(arr[i][0]), arr[i][1]))

    lst.sort(key=lambda x: x[0])

    for a in lst:
        print(a[1], end=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
