"""
* 로그파일 재정렬
1. 로그의 가장 앞 부분은 식별자이다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

- 입력
["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
- 출력
["letl art can", "let3 art zero", "let2 own kit dig", "digl 8 1 5 1", "dig2 3 6"]
"""
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = [] # 문자 로그
        digits = [] # 숫자 로그

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

if __name__ == '__main__':
    solution = Solution()
    param = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(solution.reorderLogFiles(param))
