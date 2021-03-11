from typing import List


def quick_sort(A: List[int], lo: int, hi: int):
    def partition(lo: int, hi: int):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort(A, lo, pivot - 1)
        quick_sort(A, pivot + 1, hi)
    return A


param = [2, 8, 7, 1, 3, 5, 6, 4]
print(quick_sort(param, 0, len(param) - 1))