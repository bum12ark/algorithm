"""
url: https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
* 디스크 컨트롤러
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다.
디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다.
가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청

이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.
각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때,
작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면
평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한사항
- jobs의 길이는 1 이상 500 이하입니다.
- jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
- 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
- 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
- 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

입출력 예
Input: [[0, 3], [1, 9], [2, 6]]
Output: 9

입출력 예 설명
0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.
"""
import heapq
from typing import List


def solution(jobs: List[int]) -> int:
    jobs.sort()
    total, count, current, last = 0, 0, 0, -1
    heap = []

    while count < len(jobs):
        for s, c in jobs:
            if last < s <= current:
                heapq.heappush(heap, (c, s))
        # 하나만 뽑는다. 이후에 더 짧은 시간을 갖는 job이 들어 올 수 있기 때문
        if heap:
            _cost, _start = heapq.heappop(heap)
            # 위의 for문의 if 절에 들어갈 last 변수를 초기화 (이전에 넣었던 job을 또 heap에 넣는 것을 방지)
            last = current
            current += _cost
            total += current - _start
            count += 1
        else:
            current += 1

    return total // len(jobs)


if __name__ == '__main__':
    print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))
