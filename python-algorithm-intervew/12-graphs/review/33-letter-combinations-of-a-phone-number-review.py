"""
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
* 전화 번호 문자 조합
2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.

- Example 1
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
- Example 2
Input: digits = ""
Output: []
- Example 3
Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def DFS(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in phone_number[digits[i]]:
                    DFS(i + 1, path + j)

        if not digits:
            return []

        phone_number = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = []
        DFS(0, "")

        return result


if __name__ == '__main__':
    print(Solution().letterCombinations("23"), "||", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
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