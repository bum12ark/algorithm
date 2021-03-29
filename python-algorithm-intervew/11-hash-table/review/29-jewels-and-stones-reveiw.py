"""
url: https://leetcode.com/problems/jewels-and-stones/
* 보석과 돌
J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.
- Example 1
Input : J = "aA", S = "aAAbbbb"
Output : 3
- Example 2
Input : J = "z", S = "ZZ"
Output : 0
"""
import collections


class Solution:
    def numJewelsInStonesCounter(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)

        result = 0
        for char in jewels:
            result += counter[char]

        return result

    def numJewelsInStonesDict(self, jewels: str, stones: str) -> int:
        dic = collections.defaultdict(int)

        for s in stones:
            dic[s] += 1

        result = 0
        for j in jewels:
            if j in dic:
                result += dic[j]

        return result


if __name__ == '__main__':
    jewels_1, stones_1 = "aA", "aAAbbbb"
    print(Solution().numJewelsInStonesCounter(jewels_1, stones_1), "||", 3)
    print(Solution().numJewelsInStonesDict(jewels_1, stones_1), "||", 3)

    jewels_2, stones_2 = "z", "ZZ"
    print(Solution().numJewelsInStonesCounter(jewels_2, stones_2), "||", 0)
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
