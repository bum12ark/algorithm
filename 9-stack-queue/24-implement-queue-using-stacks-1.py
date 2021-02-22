"""
* 스택을 이용한 큐 구현
스택을 이용해 다음 연산을 지원하는 큐를 구현하라
- push(x) : 요소 x를 큐 마지막에 삽입한다.
- pop() : 큐 처음에 있는 요소를 제거한다.
- peek() : 큐 처음에 있는 요소를 조회한다.
- empty() : 큐가 비어 있는지 여부를 리턴한다.

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peak() // 1리턴
queue.pop() // 1리턴
queue.empty() // false 리턴
"""

class MyQueue:
    def __init__(self):
        self.input  = []
        self.output = []


    def push(self, x: int) -> None:
        self.input.append(x)


    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # 아웃풋이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())


    def empty(self) -> bool:
        return self.input == [] and self.output == []
