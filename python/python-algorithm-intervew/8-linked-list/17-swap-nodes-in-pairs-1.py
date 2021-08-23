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
    # 값만 교환
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            # 값만 교환
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next

        return head


if __name__ == '__main__':
    solution = Solution()
    param: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(solution.swapPairs(param).print_list())
