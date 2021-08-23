import collections


def solution(lottos, win_nums):
    # 당첨 갯수: 순위
    ranking = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    # lottos와 win_nums의 갯수
    l_count = collections.Counter(lottos)
    w_count = collections.Counter(win_nums)

    worst = len(lottos) - len(w_count - l_count)
    best = worst + l_count[0]

    return [ranking[best], ranking[worst]]


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    solution(lottos, win_nums)
