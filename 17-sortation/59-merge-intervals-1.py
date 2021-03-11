"""
* 구간 병합
겹치는 구간을 병합하라.
- Example 1
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                # merged += [i]
                merged += i,
        return merged


if __name__ == '__main__':
    print(Solution().merge([[1, 3], [8, 10], [15, 18], [2, 6]]))