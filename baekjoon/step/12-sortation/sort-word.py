"""
출처: https://www.acmicpc.net/problem/1181
"""

if __name__ == '__main__':
    size = int(input())
    words = [input() for _ in range(size)]
    for w in sorted(set(words), key=lambda x: (len(x), x)):
        print(w)