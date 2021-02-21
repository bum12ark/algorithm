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


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        sorted_set = sorted(set(s))
        # 집합으로 정렬
        for char in sorted_set:
            suffix_index = s.index(char)
            suffix = s[suffix_index:]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            set_s = set(s)
            set_suffix = set(suffix)
            if set_s == set_suffix:
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


if __name__ == '__main__':
    solution = Solution()
    param = "cbacdcbc"
    print(solution.removeDuplicateLetters(param))