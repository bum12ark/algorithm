"""
출처: https://www.hackerrank.com/challenges/the-hurdle-race/problem
"""
import collections


def hurdleRace(k, height):
    deq = collections.deque(height)
    answer = 0

    while deq:
        h = deq.popleft()
        if k < h:
            answer += h - k
            k += h - k

    return answer


if __name__ == '__main__':
    print(hurdleRace(7, [2, 5, 4, 5, 2]))
