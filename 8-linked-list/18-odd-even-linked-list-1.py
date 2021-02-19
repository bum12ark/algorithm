"""
* 홀짝 연결 리스트
연결 리스트를 홀수번째 노드 다음에 짝수번째 노드가 오도록 재구성하라.
공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
- 입력 1
1->2->3->4->5->None
- 출력 1
1->3->5->2->4->None
- 입력 2
2->1->3->5->6->4->7->None
- 출력 2
2->3->6->7->1->5->4->None
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수의 헤드로 연결
        odd.next = even_head
        return head


if __name__ == '__main__':
    solution = Solution()
    param = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result: ListNode = solution.oddEvenList(param)
    result.print_list()