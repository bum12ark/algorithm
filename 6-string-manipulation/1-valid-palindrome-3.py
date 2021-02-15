"""
파이썬에서 제공하는 슬라이스 기능 사용
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식 : 문자가 아닐 경우 삭제
        s = re.sub(r'[^\w]', '', s)

        return s == s[::-1]

if __name__ == '__main__':
    solution = Solution()
    param = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(param))