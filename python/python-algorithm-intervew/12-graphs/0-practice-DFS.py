"""
주사위의 갯수를 입력 받아 나올 수 있는 모든 경우의 수를 출력하라.
"""
def dice(n: int):
    prev = []
    result = []
    def dfs(depth: int):
        if depth > n:
            result.append(prev[:])
            return

        for i in range(1, 7):
            prev.append(i)
            dfs(depth + 1)
            prev.pop()
    dfs(1)
    return result

print(dice(3))
