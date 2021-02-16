"""
* 두수의 덧셈
역순으로 저장된 연결 리스트의 숫자를 더하라
- 입력
(2->4->3) + (5->6->4)
- 출력
7 -> 0 -> 8
- 설명
342 + 465 = 807
"""
# Definition for singly-linked list.
import collections
from typing import List


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
    # 연결리스트 뒤집기 -> 재귀 사용
    def reverseList(self, head: ListNode) -> ListNode:
        pass

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        li: List[int] = []
        while node:
            li.append(node.val)
            node = node.next
        return li

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev = None
        for s in result:
            pass

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


if __name__ == '__main__':
    solution = Solution()
    param1 = ListNode(2, ListNode(4, ListNode(3)))
    param2 = ListNode(5, ListNode(6, ListNode(4)))
    solution.addTwoNumbers(param1, param2)
