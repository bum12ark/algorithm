"""
* 부분 문자열이 포함된 최소 윈도우 [복습]
문자열 S와 T를 입력받아 O(n)에 모든 문자가 포함된 S의 최소 윈도우를 찾아라.
Input: S = "ADOBECODEBANC", T = "ABC"
Output: BANC
"""
import collections
from typing import List


class Solution:
    # 투 포인터, 슬라이딩 윈도우로 최적화
    def minWindow(self, s: str, t: str) -> str:
        pass


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    s2 = "AOCOAC"
    t = "AC"
    print(Solution().minWindow(s2, t))