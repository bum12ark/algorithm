"""
url: https://leetcode.com/problems/most-common-word/
* 가장 흔한 단어
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 수미표 등) 또한 무시한다.
- Example 1
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
- Example 2
Input: paragraph = "a.", banned = []
Output: "a"
"""
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pass


if __name__ == '__main__':
    paragraph_1, banned_1 = "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
    print(Solution().mostCommonWord(paragraph_1, banned_1), "ball")
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[✓] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[✓] 중간 정도 이해함 (sorted: key=lambda)
[] 완벽히 이해함
"""