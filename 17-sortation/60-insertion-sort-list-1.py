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
        pass

if __name__ == '__main__':
    param = ListNode(4, ListNode(1, ListNode(3, ListNode(2))))
    result = Solution().insertionSortList(param)
    result.print_list()