"""
* 2D 행렬 검색 II
m * n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다.
- Example
행렬은 다음과 같다.
[
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target=5일 경우, 값이 존재하므로 true를 리턴한다.
target=20일 경우, 값이 존재하지 않으므로 false를 리턴한다.
"""
from typing import List


class Solution:
    # 첫 행의 맨 뒤에서 탐색
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(Solution().searchMatrix(matrix, target))
