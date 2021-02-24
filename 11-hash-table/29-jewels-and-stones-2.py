"""
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
    # defaultdict를 이용한 비교 생략
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in S:
            freqs[char] += 1

        for char in J:
            count += freqs[char]

        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones("aA", "aAAbbbb"))
