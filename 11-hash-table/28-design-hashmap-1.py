"""
* 해시맵 디자인
다음 기능을 제공하는 해시맵을 디자인하라.
- put(key, value) : 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
- get(key) : 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
- remove(key) : 키에 해당하는 키, 값을 해시맵에서 삭제한다.
"""
import collections


class ListNode():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap():
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        # 해시 값
        index = key % self.size

        # 해당 인덱스에 아무것도 없다면 키, 값을 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        # 해당 인덱스에 키가 존재한다면 (충돌 발생), 연결 리스트를 연결해준 뒤 종료
        p = self.table[index]
        while p:
            # 이미 키가 존재할 경우 값을 업데이트 후 종료
            if p.key == key:
                p.value = value
                return
            # p가 None이 되는 것을 방지
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # 해시 값
        index = key % self.size
        # 인덱스에 값이 존재하지 않을 경우 -1 리턴
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        # 해시 값
        index = key % self.size
        # 인덱스에 값이 존재하지 않을 경우 -1 리턴
        if self.table[index].value is None:
            return -1
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        while p:
            if p.key == key:
                # 삼항 연산자
                self.table[index] = ListNode() if p.next is None else p.next
                return
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next