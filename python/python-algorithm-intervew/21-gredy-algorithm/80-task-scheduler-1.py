"""
* 태스크 스케줄러 [복습]
A에서 Z로 표현된 태스크가 있다.
각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고, n번의 간격 내에는 동일한 태스크를 실행할 수 없다.
더 이상 태스크를 실행할 수 없는 경우 아이들(idle)상태가 된다.
모든 태스크를 실행하기 위한 최소 간격을 출력하라.
- Example
Input: tasks = ["A", "A", "A", "B", "B", "B", "B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
"""
import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


if __name__ == '__main__':
    task = ["A", "A", "A", "B", "B", "B", "B"]
    n = 2
    Solution().leastInterval(task, n)