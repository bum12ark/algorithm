"""
* 해시맵 디자인
다음 기능을 제공하는 해시맵을 디자인하라.
- push(key, value) : 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
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

    def push(self, key, value):
        pass

    def get(self, key):
        pass

    def remove(self, key):
        pass