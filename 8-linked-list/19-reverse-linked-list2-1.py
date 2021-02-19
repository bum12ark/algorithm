"""
인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
- 입력
1->2->3->4->5->None, m = 2, n = 4
- 출력
1->4->3->2->5->None
"""


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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next = current.next
            next.next = current
            current.next = next.next
            prev =
        pass



    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pass