"""
* 두 정렬 리스트의 병합
- 입력
1->2->4, 1->3->4
- 출력
1->1->2->3->4->4
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            cur = self.mergeTwoLists(l1.next, l2)
            l1.next = cur
        return l1


if __name__ == '__main__':
    solution = Solution()
    param1 = ListNode(1, ListNode(2, ListNode(4)))
    param2 = ListNode(1, ListNode(3, ListNode(4)))
    result = solution.mergeTwoLists(param1, param2)
    print(result.print_list())
