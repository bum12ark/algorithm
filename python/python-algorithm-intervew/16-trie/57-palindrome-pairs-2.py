"""
* 팰린드롬 페어 [복습]
단어 리스트에서 words[i] + words[j]가 팰린드롬이 되는 모든 인덱스 조합 (i, j)를 구하라
- Example 1
Input: ["abcd", "dcba", "lls", "s", "sssll"]
Output: [[0, 1], [1, 0], [3, 2], [2, 4]]
Explanation: ["dcbaabcd", "abcddcba", "slls", "llsssssll"]이 팰린드롬이다.
- Example 2
Input: ["bat", "tab", "cat"]
Output: [[0, 1], [1, 0]]
Explanation: ["battab", "tabbat"]이 팰린드롬이다.
"""
import collections
from typing import List


class Solution:
    # 트라이로 구현
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    param1: List[str] = ["abcd", "dcba", "lls", "s", "sssll"]
    param2: List[str] = ["bat", "tab", "cat"]

    print(Solution().palindromePairs(param1))
    print(Solution().palindromePairs(param2))
