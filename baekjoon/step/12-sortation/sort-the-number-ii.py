"""
출처: https://www.acmicpc.net/problem/2751
"""
import sys
from typing import List


def merge_sort(lst: List[int]):
    def devide(low, high):
        if low < high:
            mid = low + (high - low) // 2
            devide(low, mid)
            devide(mid + 1, high)
            merge(low, mid, high)

    def merge(start, mid, end):
        temp = [0] * len(lst)
        for i in range(start, end + 1):
            temp[i] = lst[i]

        part1 = start
        part2 = mid + 1
        index = start
        while part1 <= mid and part2 <= end:
            if temp[part1] <= temp[part2]:
                lst[index] = temp[part1]
                part1 += 1
            else:
                lst[index] = temp[part2]
                part2 += 1
            index += 1

        for i in range(mid - part1 + 1):
            lst[index + i] = temp[part1 + i]

    devide(0, len(lst) - 1)

    return lst


if __name__ == '__main__':
    # test = [4, 2, 6, 3, 7, 8, 5, 1]
    size = int(sys.stdin.readline())
    nums = []
    for _ in range(size):
        nums.append(int(sys.stdin.readline()))
    print(merge_sort(nums))
