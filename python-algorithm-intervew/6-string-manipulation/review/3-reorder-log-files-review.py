"""
url: https://leetcode.com/problems/reorder-data-in-log-files/
* 로그파일 재정렬
1. 로그의 가장 앞 부분은 식별자이다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

- Example 1:
Input: ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["letl art can", "let3 art zero", "let2 own kit dig", "digl 8 1 5 1", "dig2 3 6"]
"""

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log = []
        letter_log = []

        for _log in logs:
            if _log.split()[1].isdigit():
                digit_log.append(_log)
            else:
                letter_log.append(_log)

        letter_log.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_log + digit_log


if __name__ == '__main__':
    print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
          , ["letl art can", "let3 art zero", "let2 own kit dig", "digl 8 1 5 1", "dig2 3 6"])
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