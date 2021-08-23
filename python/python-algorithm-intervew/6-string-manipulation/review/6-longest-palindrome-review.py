"""
url: https://leetcode.com/problems/longest-palindromic-substring/
* 가장 긴 팰린드롬 문자열

- Example 1
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def _expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s) - 1):
            result = max(result,
                         _expand(i, i + 1),
                         _expand(i, i + 2),
                         key=len)
        return result


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"), "bab")
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