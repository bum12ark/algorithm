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
        # 중복을 제거한 제일 먼저오는 알파벳 순서를 가져오기 위한 set
        sorted_set = sorted(set(s))
        # 집합으로 정렬
        for char in sorted_set:
            suffix_index = s.index(char)
            suffix = s[suffix_index:]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행 (중복을 제거하기 위함)
            set_s = set(s)
            set_suffix = set(suffix)
            if set_s == set_suffix:
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


if __name__ == '__main__':
    solution = Solution()
    param = "cbacdcb"
    print(solution.removeDuplicateLetters(param))