"""
* 쿠키 부여
아이들에게 1개씩 쿠키를 나눠줘야 한다.
각 아이 child_i 마다 그리드 팩터 g를 갖고 있으며, 이는 아이가 만족하는 최소 쿠키의 크기를 말한다.
각 쿠키 cookie_j는 크기 s를 갖고 있으며 s >= g 이어야 아이가 만족하며 쿠키를 받는다.
최대 몇 명의 아이들에게 쿠키를 줄 수 있는지 출력하라.
- Example 1
Input: [1, 2, 3], [1, 1]
Output:  1
Explanation: 두 번째 아이부터는 크기 2 이상의 쿠키가 필요하지만,
             갖고 있는 최대 크기는 1이기 때문에 1명의 아이에게만 줄 수 있다.
- Example 2
Input: [1, 2], [1, 2, 3]
Output: 2
Explanation: 충분한 쿠키를 갖고 있고, 2명 모두에게 쿠키를 줄 수 있다.
"""
from typing import List


class Solution:
    # 이진 검색으로 구현
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        pass


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    print(Solution().findContentChildren(g, s))