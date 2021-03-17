"""
* 계단 오르기
당신은 계단을 오르고 있다. 정상에 도달하기 위해 n 계단을 올라야 한다.
매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇 가지 경로가 되는지 계산하라.
- Example
Input: 3
Output: 3
Explanation: 정상에 오르기 위한 방법은 3가지 경로가 있다.
    a. 1계단 + 1계단 + 1계단
    b. 1계단 + 2계단
    c. 2계단 + 1계단
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    print(Solution().climbStairs(4))