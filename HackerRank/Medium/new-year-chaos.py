"""
출처: https://www.hackerrank.com/challenges/new-year-chaos/problem
"""
import collections


def minimumBribes_mine(q):
    dic = collections.defaultdict(int)  # 새치기하기 전 위치
    for i, v in enumerate(sorted(q)):
        dic[v] = i

    answer = 0
    min_val = q[len(q) - 1]  # 최소값 제일 뒤의 값
    for i in range(len(q) - 2, -1, -1):
        if q[i] > min_val:
            cut_in_count = q.index(min_val) - i
            if cut_in_count > 2:
                return "Too chaotic"
            answer += cut_in_count
        min_val = min(min_val, q[i])

    return answer


def minimumBribes(q):
    dic = collections.defaultdict(int)  # 새치기하기 전 위치
    for i, v in enumerate(sorted(q)):
        dic[v] = i
    print(dic)

    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        #  원래 자리에서 앞으로 두칸 이상 이동 시 검증
        if dic[q[i]] - i > 2:  # 원래 자리에서 얼만큼 이동했는지
            return 'Too chaotic'

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    return bribes


if __name__ == '__main__':
    # q = [2, 1, 5, 6, 3, 4, 9, 8, 11, 7, 10]
    q = [2, 1, 5, 3, 4]
    print("=======answer=======")
    print(minimumBribes_mine(q))
    print(minimumBribes(q))