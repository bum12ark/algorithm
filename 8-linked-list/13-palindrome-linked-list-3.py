"""
* 팰린드롬 연결 리스트
연결 리스트가 팰린드롬 구조인지 판별하라.
- 입력
1->2->2->1
- 출력
true
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 런너를 이용한 우아한 풀이
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next  # 두 칸씩 이동
            rev, rev.next, slow = slow, rev, slow.next
        # 홀수 일 경우 포인터를 한 칸 더 앞으로 이동하여 중앙의 값을 빗겨나가야한다.
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev  # 끝까지 이동했을 경우 None이기 때문에 not rev 또는 not slow 둘다 가능하다.


if __name__ == '__main__':
    solution = Solution()
    param = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(solution.isPalindrome(param))
