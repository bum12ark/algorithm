"""
출처: https://www.acmicpc.net/problem/11651
"""

if __name__ == '__main__':
    size = int(input())
    result = []
    for _ in range(size):
        x, y = map(int, input().split())
        result.append((x, y))

    for x, y in sorted(result, key=lambda k: (k[1], k[0])):
        print(x, y)