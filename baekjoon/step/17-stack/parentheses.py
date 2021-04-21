"""
출처: https://www.acmicpc.net/problem/9012
"""
import sys

s = "(())())"

table = {
    ")": "("
}


def valid_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


if __name__ == '__main__':
    size = int(sys.stdin.readline().rstrip())
    for _ in range(size):
        p = sys.stdin.readline().rstrip()
        print("YES") if valid_parentheses(p) else print("NO")
