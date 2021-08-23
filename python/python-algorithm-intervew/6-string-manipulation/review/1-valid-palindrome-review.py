"""
url: https://leetcode.com/problems/valid-palindrome/
* 유효한 팰린드롬
주어진 문자열이 팰린드롬인지 확인하라.
대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

- 예제 1:
입력: "A man, a plan, a canal: Panama"
출력: true
- 예제 2:
입력: "race a car"
출력: false
"""
import collections
import re


class Solution:
    def isPalindromeDequeue(self, s: str) -> bool:
        deq = collections.deque()
        for _s in s:
            if _s.isalnum():
                deq.append(_s.lower())

        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False
        return True

    def isPalindromeSlicing(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^\w]', '', s)
        return s == s[::-1]


if __name__ == '__main__':
    print(Solution().isPalindromeSlicing("A man, a plan, a canal: Panama"), True)
    print(Solution().isPalindromeSlicing("race a car"), False)

    print(Solution().isPalindromeSlicing("ab_a"), True)

    print(Solution().isPalindromeDequeue("A man, a plan, a canal: Panama"), True)
    print(Solution().isPalindromeDequeue("race a car"), False)

"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[✓] 코드 완성
 
[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""
