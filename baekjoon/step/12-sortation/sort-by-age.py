"""
출처: https://www.acmicpc.net/problem/10814
"""

if __name__ == '__main__':
    size = int(input())
    persons = []
    for i in range(size):
        age, name = map(str, input().split())
        persons.append((i, int(age), name))

    for idx, age, name in sorted(persons, key=lambda x: (x[1], x[0])):
        print(age, name)