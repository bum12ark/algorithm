"""
* 원형 큐 디자인
원형 큐를 디자인해라

MyCircularQueue circularQueue = new MyCircularQueue(5); // 크기를 5로 지정
circularQueue.enQueue(10); // true 리턴
circularQueue.enQueue(20); // true 리턴
circularQueue.enQueue(30); // true 리턴
circularQueue.enQueue(40); // true 리턴
circularQueue.Rear(); // 40 리턴
circularQueue.isFull(); // false 리턴
circularQueue.deQueue(); // true 리턴
circularQueue.deQueue(); // true 리턴
circularQueue.enQueue(50); // true 리턴
circularQueue.enQueue(60); // true 리턴
circularQueue.Rear(); // 60 리턴
circularQueue.Front(); // 30 리턴
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.max_len = k # 최대 길이
        self.p1 = 0 # front 포인터
        self.p2 = 0 # rear 포인터

    # 리어 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.max_len
            return True
        else:
            return False

    # 프론트 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p] = None
            self.p1 = (self.p1 + 1) % self.max_len
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.q[self.p1] is None and self.p1 == self.p2

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None

if __name__ == '__main__':
    circularQueue = MyCircularQueue()