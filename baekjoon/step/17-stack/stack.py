"""
출처: https://www.acmicpc.net/problem/10828
"""
import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n: int) -> None:
        self.stack.append(n)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def size(self) -> int:
        return len(self.stack)

    def empty(self) -> int:
        return 1 if not self.stack else 0

    def top(self):
        return self.stack[len(self.stack) - 1] if self.stack else -1


if __name__ == '__main__':
    s = Stack()

    size = int(sys.stdin.readline().rstrip())
    for _ in range(size):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == "push":
            s.push(command[1])
        elif command[0] == "pop":
            print(s.pop())
        elif command[0] == "size":
            print(s.size())
        elif command[0] == "empty":
            print(s.empty())
        elif command[0] == "top":
            print(s.top())
