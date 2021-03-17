"""
* 배낭 문제
짐을 쪼갤 수 없다.
cargo = (짐의 가치, 무게), capacity = 담을 수 있는 배낭의 무게
"""
class Solution:
    def zero_one_knapsack(self, cargo, capacity):
        pack = []

        for i in range(len(cargo) + 1):
            pack.append([])
            for c in range(capacity + 1):
                if i == 0 or c == 0:
                    pack[i].append(0)
                elif cargo[i - 1][1] <= c:
                    pack[i].append((
                        max(
                            cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                            pack[i - 1][c]
                        ))
                    )
                else:
                    pack[i].append(pack[i - 1][c])
        for p in pack:
            print(p)
        return pack[-1][-1]


if __name__ == '__main__':
    cargo = [
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2)
    ]
    capacity = 15
    print(Solution().zero_one_knapsack(cargo, capacity))