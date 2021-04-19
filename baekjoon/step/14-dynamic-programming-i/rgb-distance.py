"""
출처: https://www.acmicpc.net/problem/1149
"""
# param
size = int(input())
RGB = [list(map(int, input().split())) for _ in range(size)]

for idx in range(1, len(RGB)):
    RGB[idx][0] = min(RGB[idx - 1][1], RGB[idx - 1][2]) + RGB[idx][0]
    RGB[idx][1] = min(RGB[idx - 1][0], RGB[idx - 1][2]) + RGB[idx][1]
    RGB[idx][2] = min(RGB[idx - 1][0], RGB[idx - 1][1]) + RGB[idx][2]

print(min(RGB[size - 1]))