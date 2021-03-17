"""
데크 사용
"""
import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 데크 선언
        deq: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                deq.append(char.lower())

        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    param = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(param))