"""
* 부분 문자열이 포함된 최소 윈도우
문자열 S와 T를 입력받아 O(n)에 모든 문자가 포함된 S의 최소 윈도우를 찾아라.
Input: S = "ADOBECODEBANC", T = "ABC"
Output: BANC
"""
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_substr_lst: List, t_lst: List) -> bool:
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True

        window_size = len(t)

        # 슬라이딩 윈도우 증가
        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr

        return ''

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))