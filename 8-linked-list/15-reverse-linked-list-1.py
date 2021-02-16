"""
* 역순 연결리스트
연결 리스트를 뒤집어라
Input : 1->2->3->4->5->NULL
Output : 5->4->3->2->1->NULL
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
    # 재귀 구조로 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        # prev : 리턴할 값
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            # next : 노드의 다음 값
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


if __name__ == '__main__':
    solution = Solution()
    param = ListNode(1, ListNode(2, ListNode(3)))
    print(solution.reverseList(param).print_list())