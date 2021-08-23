"""
출처: https://www.hackerrank.com/challenges/the-grid-search/problem
"""


# 첫번째 로우가 어러개 있을 경우를 생각하지 않음
def gridSearch_Fail(G, P):
    # Write your code here
    start = end = row = 0
    grid = []
    for i in range(len(G)):
        if P[0] in G[i]:
            row = i
            start = G[i].index(P[0])
            end = start + len(P[0])

        if i < len(P) + row and start and end:
            grid.append(G[i][start: end])

    if grid == P:
        return "YES"

    return "NO"


def gridSearch(G, P):
    def check(x, y):
        for i in range(len(P)):
            if P[i] != G[x + i][y: y + len(P[i])]:
                return False
        return True

    for i in range(len(G)):
        for j in range(len(G[i])):
            if P[0][0] in G[i][j]:
                if check(i, j):
                    return "YES"
    return "NO"


G = [
    "7283455864",
    "6731158619",
    "8988242643",
    "3830589324",
    "2229505813",
    "5633845374",
    "6473530293",
    "7053106601",
    "0834282956",
    "4607924137"
]
P = [
    "9505",
    "3845",
    "3530"
]

print(gridSearch(G, P))
