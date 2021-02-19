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
    '''
    root : 리턴 값
    head : 바꿀 첫 번째 노드
    b : 바꿀 두 번째 노드
    prev : 바꿀 첫 번째 노드의 이전 노드
    ex) prev -> head -> b
    '''
    # 반복 구조로 스왑
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록
            prev.next = b

            # 다음 번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next


if __name__ == '__main__':
    solution = Solution()
    param = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    result = solution.swapPairs(param)
    result.print_list()
