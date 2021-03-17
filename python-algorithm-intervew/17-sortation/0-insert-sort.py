from typing import List


def insert_sort(lst: List[int]):
    for i in range(1, len(lst)):
        j = i - 1
        key = lst[i]

        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key
    return lst
