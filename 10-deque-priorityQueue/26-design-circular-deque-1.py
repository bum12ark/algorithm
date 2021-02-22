"""
* 원형 데크 디자인
다음 연산을 제공하는 원형 데크를 디자인하라.
MyCircularEdque(k) : 데크 사이즈를 k로 지정하는 생성자다.
insertFront() : 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴한다.
insertLast() : 데크 마지막에 아이템을 추가하고 성공할 경우 true를 리턴한다.
deleteFront() : 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
deleteLast() : 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
getFront() : 데크의 첫 번째 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
getRear() : 데크의 마지막 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
isEmpty() : 데크가 비어 있는지 여부를 판별한다.
isFull() : 데크가 가득 차 있는지 여부를 판별한다.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyCirCularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0 # k : 최대 길이 정보, len : 현재 길이 정보
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    # 앞쪽에 노드를 추가
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True