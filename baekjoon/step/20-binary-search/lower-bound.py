"""
입력받은 수 이상의 값이 정렬된 배열(arr)에서 처음으로 등장하는 위치를 찾는 알고리즘
시간 복잡도: O(logn)
공간 복잡도: O(n)
사용한 알고리즘: LowerBound(이진 탐색)
사용한 자료구조: 1차원 배열
"""
import sys

target = 6
result = sys.maxsize
arr = [1, 2, 2, 2, 4, 4]

def lower_bound(left, right):
    while left <= right:
        mid = left + (right - left) // 2
        # 찾고자 하는 값보다 작으면, mid 이하를 버립니다.
        if arr[mid] < target:
            left = mid + 1
        # 찾고자 하는 값보다 크면, mid 이상을 버립니다.
        # 찾고자 하는 값 이상이 처음으로 등장하는 위치를 찾기 때문에 가장 작은 인덱스를 갱신합니다.
        else:
            result = min(result, mid)
            right = mid - 1
