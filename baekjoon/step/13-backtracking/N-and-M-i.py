"""
출처: https://www.acmicpc.net/problem/15649
"""

prev_element = []
result = []


def sequence(element, length):
    # 탈출
    if length == 0:
        # result.append(prev_element.copy())
        print(' '.join(map(str, prev_element)))
        return

    for e in element:
        next_element = element.copy()
        next_element.remove(e)

        prev_element.append(e)
        sequence(next_element, length - 1)
        prev_element.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    N_list = [x + 1 for x in range(N)]
    sequence(N_list, M)
