import collections
import heapq
from typing import List


class Solution:
    def myNetworkDelayTime(self, times:List[List[int]], N: int, K: int) -> int:
        grapgh = collections.defaultdict(list)

        for _from, _to, time in times:
            grapgh[_from].append((_to, time))

        # [(소요시간, 시작노드)]. 소요시간 기준으로 heapq에서 데이터를 뽑아낸다.
        queue = [(0, K)]
        # 노드에 도착한 시간을 저장할 dictionary
        arrived = collections.defaultdict(int)

        while queue:
            time, node = heapq.heappop(queue)
            if node not in arrived:
                arrived[node] = time
                # 다음으로 이동할 수 있는 노드 탐색
                for _next, delay in grapgh[node]:
                    arrive_time = time + delay
                    heapq.heappush(queue, (arrive_time, _next))

        if len(arrived) == N:
            return max(arrived.values())
        return -1


    def networkDelayTime(self, times:List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 우선순위 큐 [(소요시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.networkDelayTime([[3,1,5], [3,2,2], [2,1,2], [3,4,1], [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1]], 8, 3))
    print(solution.myNetworkDelayTime([[3,1,5], [3,2,2], [2,1,2], [3,4,1], [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1]], 8, 3))