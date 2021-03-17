"""
* 그룹 애너그램
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

- 입력
["eat", "tea", "tan", "ate", "nat", "bat"]
- 출력
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"],
]
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list) # list를 value로 가지는 defaultdict 선언

        for s in strs:
            dic[''.join(sorted(s))].append(s)

        return list(dic.values())

if __name__ == '__main__':
    solution = Solution()
    param: List[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(param))