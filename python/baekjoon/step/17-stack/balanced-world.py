"""
출처: https://www.acmicpc.net/problem/4949
"""
import sys


table = {
    ")": "(",
    "]": "["
}


def valid_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char in table.values():
            stack.append(char)
        elif char in table and (not stack or table[char] != stack.pop()):
            return False
    return len(stack) == 0


if __name__ == '__main__':
    while True:
        p = sys.stdin.readline().rstrip()
        if p == ".":
            break
        print("yes") if valid_parentheses(p) else print("no")
