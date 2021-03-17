from typing import List


def bubble_sort(words: List[str]):
    for i in range(1, len(words)):
        for j in range(0, len(words) - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]