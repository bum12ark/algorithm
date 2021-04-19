"""
출처: https://www.acmicpc.net/problem/12865
"""
# 1. param
size, capacity = map(int, input().split())
cargo = []
for _ in range(size):
    w, v = map(int, input().split())
    cargo.append((v, w))

# 2.
# 0으로 초기화
pack = [[0 for _ in range(capacity + 1)] for _ in range(size + 1)]
for i in range(1, size + 1):
    for c in range(1, capacity + 1):
        current_weight = cargo[i - 1][1]
        if current_weight <= c:
            current_value = cargo[i - 1][0]
            pack[i][c] = max(
                    current_value + pack[i - 1][c - current_weight],
                    pack[i - 1][c]
                )
        else:
            pack[i][c] = pack[i - 1][c]

print(pack[-1][-1])
