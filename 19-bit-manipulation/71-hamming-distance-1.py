"""
* 해밍거리
두 정수를 입력받아 몇 비트가 다른지 계산하라
- Example
Input: x = 1, y = 4
Output: 2
Explanation:
1 (0 0 0 1)
4 (0 1 0 0)
     *   *
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 4))