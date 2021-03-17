"""
* 가장 흔한 단어
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 수미표 등) 또한 무시한다.
- 입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
- 출력
"ball"
"""
import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 리스트 컨프리핸션 사용
        paragraph = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                     if word not in banned]
        counter = collections.Counter(paragraph)
        # 제일 많이 카운터된 객체 리턴 -> 첫번째 인덱스 리턴 (ball, 2)
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    solution = Solution()
    param1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    param2 = ["hit"]
    print(solution.mostCommonWord(param1, param2))
