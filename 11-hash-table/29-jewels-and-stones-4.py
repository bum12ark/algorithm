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


class Solution:
    # 파이썬다운 방식 (리스트 컴프리핸션 사용)
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones("aA", "aAAbbbb"))