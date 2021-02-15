"""
스택 사용
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    param = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(param))