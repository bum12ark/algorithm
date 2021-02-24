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

class MyCirCularDeque:
    def __init__(self, k: int):
        # head와 tail은 고정 값으로 아무 값을 지니고 있지 않다.
        # 즉 맨 앞과 맨 뒤를 의미한다.
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0 # k : 최대 길이 정보, len : 현재 길이 정보
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.rihgt
        node.right = new
        new.left, new.right = node, n
        n.left = node

    # 입력 받은 노드의 다음 노드 삭제
    def _delete(self, node:ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    # 앞쪽에 노드를 추가
    def insertFront(self, value: int) -> bool:
        if self.len == self.k: # 더이상 추가할 노드가 없다면
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    # 뒤쪽에 노드를 추가
    def insertLast(self, value: int) -> bool:
        if self.len == self.k: # 더 이상 추가할 노드가 없다면
            return False
        self.len -= 1
        self._add(self.tail.left, ListNode(value))
        return True

    # 앞쪽 노드 삭제
    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._delete(self.head)
        return True
    
    # 뒤쪽 노드 삭제
    def delteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._delete(self.tai.left.left)
        return True

    # 첫번째 노드를 가져온다.
    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    # 마지막 노드를 가져온다.
    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    # 데크가 비어 있는 지 여부를 판단한다.
    def isEmpty(self) -> bool:
        return self.len == 0

    # 데크가 가득 차 있는 지 여부를 판단한다.
    def isFull(self) -> bool:
        return self.len == self.k

