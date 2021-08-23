"""
url: https://leetcode.com/problems/group-anagrams/
* 그룹 애너그램
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

- Example 1
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for word in strs:
            dic[''.join(sorted(word))].append(word)

        return list(dic.values())


if __name__ == '__main__':
    param = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(param), [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
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
