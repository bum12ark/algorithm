"""
* 페어의 노드스왑
연결 리스트를 입력받아 페어 단위로 스왑하라.
- 입력
1->2->3->4
- 출력
2->1->4->3
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
    # 재귀 구조로 스왑
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값을 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head


if __name__ == '__main__':
    solution = Solution()
    param = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    result = solution.swapPairs(param)
    result.print_list()
