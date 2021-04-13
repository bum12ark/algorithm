"""
출처: https://www.acmicpc.net/problem/11650
"""

if __name__ == '__main__':
    size = int(input())
    result = []
    for _ in range(size):
        x, y = map(int, input().split())
        result.append((x, y))
    print(sorted(result))
    for x, y in sorted(result):
        print(x, y)