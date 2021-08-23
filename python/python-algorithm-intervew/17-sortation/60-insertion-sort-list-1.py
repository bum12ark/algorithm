"""
* 삽입 정렬 리스트
연결 리스트를 삽입 정렬로 정렬하라.
"""


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
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            # 커서 이동
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # 스왑
            cur.next, head.next, head = head, cur.next, head.next

            # inner while에서 이동한 cur의 포인터를 처음부터 비교하기 위해 맨 처음으로 옮기기
            cur = parent
        return parent.next or cur.next

if __name__ == '__main__':
    param = ListNode(4, ListNode(1, ListNode(3, ListNode(2))))
    result = Solution().insertionSortList(param)
    result.print_list()