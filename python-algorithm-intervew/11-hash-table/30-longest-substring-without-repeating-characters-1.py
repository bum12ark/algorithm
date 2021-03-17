"""
* 중복 문자 없는 가장 긴 부분 문자열
중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.
- Example 1
Input : "abcabcbb"
Output : 3
- Example 2
Input : "bbbbb"
Output : 1
- Example 3
Input : "pwwkew"
Output : 3
"""


class Solution:
    # 슬라이딩 윈도우와 투 포인터로 사이즈 조절
    def lengthOfLongestSubstring(selfself, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자이고 슬라이딩 문자열 전이라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            # 최대 부분 문자열 길이 갱신
            else:
                max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

        return max_length
