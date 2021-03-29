"""
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
* 중복 문자 없는 가장 긴 부분 문자열
중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.

- Example 1
Input : "abcabcbb"
Output : 3
Explanation: The answer is "abc", with the length of 3.
- Example 2
Input : "bbbbb"
Output : 1
- Example 3
Input : "pwwkew"
Output : 3
Explanation: The answer is "wke", with the length of 3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        used = {}
        max_length = start = 0
        for idx, val in enumerate(s):
            if val in used and start <= used[val]:
                start = used[val] + 1
            else:
                max_length = max(max_length, idx - start + 1)
            used[val] = idx

        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"), "||", 3)
    print(Solution().lengthOfLongestSubstring("tmmzuxt"), "||", 5)
"""
[시작 체크 리스트]
[✓] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""
