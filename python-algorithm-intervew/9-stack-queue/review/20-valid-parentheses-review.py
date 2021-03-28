"""
url: https://leetcode.com/problems/valid-parentheses/
* 유효한 괄호
괄호로 된 입력값이 올바른지 판별하라
- Example
Input: s = "()[]{}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for value in s:
            if value not in dic:
                stack.append(value)
            elif not stack and stack.pop() != dic[value]:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid("()"), True)
    print(Solution().isValid("{[]}"), True)
    print(Solution().isValid("(]"), False)
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[✓] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""