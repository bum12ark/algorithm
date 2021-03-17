"""
* 주유소
원형으로 경로가 연결된 주유소 목록이 있다.
각 주유소는 gas[i]만큼의 기름을 갖고 있으며, 다름 주유소로 이동하는데 cost[i]가 필요하다.
기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 방문할 수 있는 출발점의 인덱스를 출력하라.
출발점이 존재하지 않을 경우 -1을 리턴하며, 출발점은 유일하다.
- Example 1
Input: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
Output: 3
Explanation:
3번 인덱스(기름을 4번만큼 충전할 수 있는)에서 출발할 경우는 다음과 같다.
3번 -> 4번  +4  -1  fuel  3
4번 -> 0번  +5  -2  fuel  6
0번 -> 1번  +1  -3  fuel  4
1번 -> 2번  +2  -4  fuel  2
2번 -> 3번  +3  -5  fuel  0
정확히 기름이 0까지 소모되며, 모든 주유소를 방문할 수 있다.
"""
from typing import List


class Solution:
    # 한번만 방문 - 수학적 귀류법으로 접근
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        fuel = start = 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(gas, cost))
