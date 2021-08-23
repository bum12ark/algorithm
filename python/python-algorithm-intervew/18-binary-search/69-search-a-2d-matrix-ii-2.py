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
    # 파이썬다운 방식
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # any()는 포함된 값 중 어느 하나가 참이라면 항상 참으로 출력한다. 논리 연산의 OR와 비슷
        # any([True, False, False]) -> True
        # all()은 모든 값이 참이어야 True를 출력한다. 논리 연산의 AND와 유사하다.
        # all([True, False, False]) -> False, all([True, True, True]) -> True
        return any(target in row for row in matrix)


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
