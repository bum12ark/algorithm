"""
* k개 정렬 리스트 병합
k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
- 입력
[
    1->4->5,
    1->3->4,
    2->6
]
- 출력
1->1->2->3->4->-4->5->6
- 설명
여기서 k는 3이다.
"""
import heapq
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        cur = self
        while cur:
            print(cur.val, end='->')
            cur = cur.next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, list[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

if __name__ == '__main__':
    solution = Solution()
    param = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    rst = solution.mergeKLists(param)
    rst.print_list()