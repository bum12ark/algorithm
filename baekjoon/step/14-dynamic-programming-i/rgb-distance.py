"""
출처: https://www.acmicpc.net/problem/1149
"""
# param
size = int(input())
triangle = [list(map(int, input().split())) for _ in range(size)]

# 2번째 로우부터 시작
for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        # 첫번 째 줄
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        # 마지막 줄
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j],
                                  triangle[i - 1][j - 1])

print(max(triangle[size - 1]))

