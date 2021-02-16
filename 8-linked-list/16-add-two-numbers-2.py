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
    # 전가산기구현
    def addTwoNumbers(selfself, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0 # 자리올림수
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫 (자리올림수_과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

if __name__ == '__main__':
    solution = Solution()
    param1 = ListNode(2, ListNode(4, ListNode(5)))
    param2 = ListNode(5, ListNode(6, ListNode(4)))
    print(solution.addTwoNumbers(param1, param2).print_list())