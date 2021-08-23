"""
출처: https://www.acmicpc.net/problem/1874
"""
import sys
from typing import List


def valid_sequence(nums: List[int]) -> bool:
    count = 0
    stack = []
    for n in nums:
        while count < n:
            count += 1
            stack.append(count)
            result.append("+")

        if n == stack[-1]:
            stack.pop()
            result.append("-")
        else:
            return False
    return True


result = []
if __name__ == '__main__':
    size = int(sys.stdin.readline().rstrip())
    p = [int(sys.stdin.readline().rstrip()) for _ in range(size)]
    if valid_sequence(p):
        print("\n".join(result))
    else:
        print("NO")
