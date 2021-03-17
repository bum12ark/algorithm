"""
* 리스트 정렬
연결 리스트를 O(n log n)에 정렬하라.
- Example 1
Input: 4->2->1->3
Output: 1->2->3->4
"""

# Definition for singly-linked list.
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


# 내장 함수를 이용하는 실용적인 방법
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 연결리스트 -> 리스트
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head


if __name__ == '__main__':
    param = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    result = Solution().sortList(param)
    result.print_list()