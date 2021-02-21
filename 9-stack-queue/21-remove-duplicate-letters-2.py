"""
* 중복 문자 제거
중복된 문자를 제외하고 사전식 순서로 나열하라.
예제 1
- 입력
"bcabc"
- 출력
"abc"
예제 2
- 입력
"cbacdcbc"
- 출력
"acdb"
"""
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            # 같은게 있으면 추가 X
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            # 1. 붙일 문자가 바로 앞보다 작은가
            # 2. 뒤에 앞에 문자가 남아 있는가
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution()
    param = "cbacdcbc"
    print(solution.removeDuplicateLetters(param))