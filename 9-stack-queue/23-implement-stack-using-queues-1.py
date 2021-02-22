"""
* 큐를 이용한 스택 구현
큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
- push(x) : 요소 x를 스택에 삽입한다.
- pop() : 스택의 첫 번째 요소를 삭제한다.
- top() : 스택의 첫 번째 요소를 가져온다.
- empty() : 스택이 비어 있는지 여부를 리턴한다.

MyStack stack = new Stack();
stack.push(1);
stack.push(2);
stack.top(); // 2리턴
stack.pop(); // 2리턴
stack.empty(); // false 리턴
"""
import collections


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())