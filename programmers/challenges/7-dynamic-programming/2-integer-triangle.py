"""
* 정수 삼각형
"""
import collections

sum = 0
def solution(triangle):
    prev_element = []
    def DFS(index, depth):
        if depth == len(triangle):
            return

        for _idx, _val in enumerate(dic[depth]):
            prev_element.append(dic[depth][index])
            DFS(_idx, depth + 1)
            DFS(_idx + 1, depth + 1)

    dic = {}
    for idx, val in enumerate(triangle):
        if idx not in dic:
            dic[idx] = val

    DFS(0, 0)



if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
