"""
* 전화 번호 문자 조합
2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
- Example 1
Input : 2, 3
Output : ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        dfs(0, "")

        return result

if __name__ == '__main__':
    solution = Solution()
    param = "23"
    print(solution.letterCombinations(param))