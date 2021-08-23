"""
* 정수 삼각형
"""
import collections

def solution(triangle):
    sum_list = [[0 for x in range(y)] for y in range(1, len(triangle) + 1)]
    sum_list[0][0] = triangle[0][0]
    def DFS(depth, index):
        if depth == len(triangle) - 1:
            return triangle[depth][index]

        if sum_list[depth + 1][index] != 0:
            next1 = sum_list[depth + 1][index]
        else:
            next1 = DFS(depth + 1, index)

        if sum_list[depth + 1][index + 1] != 0:
            next2 = sum_list[depth + 1][index + 1]
        else:
            next2 = DFS(depth + 1, index + 1)

        sum_list[depth][index] = max(
            triangle[depth][index] + next1,
            triangle[depth][index] + next2
        )
        return sum_list[depth][index]

    DFS(0, 0)
    return sum_list[0][0]


def best_solution(triangle):
    def f(triangle, i, j, memo):
        if i == len(triangle) - 1:
            return triangle[i][j]

        if (i, j) in memo:
            return memo[(i, j)]

        a = f(triangle, i + 1, j, memo)
        b = f(triangle, i + 1, j + 1, memo)
        x = triangle[i][j] + max(a, b)

        memo[(i, j)] = x

        return x

    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer

if __name__ == '__main__':
    # print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
    print(best_solution([[7], [3, 8], [8, 1, 0]]))
