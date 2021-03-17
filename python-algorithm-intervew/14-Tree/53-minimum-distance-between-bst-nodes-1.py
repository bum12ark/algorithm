"""
* 이진 탐색 트리(BST) 노드 간 최소 거리
두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.
- Example 1
Input: root = [4, 2, 6, 1, 3, null, null]
Output: 1
Explanation:
[4, 2, 6, 1, 3, null, null]은 다음과 같은 트리로 표현할 수 있다.
      4
   /    \
  2      6
 / \
1   3
노드 3과 노드 4의 값의 차이는 1이다.
- Example 2
Input: root = [10, 4, 15, 1, 8, null, null]
Output: 2
-Explanation:
[10, 4, 15, 1, 8, null, null]은 다음과 같은 트리로 표현할 수 있다.
      10
   /    \
  4      15
 / \
1   8
이 경우 노드 간 값 차이가 가장 적은 노드는 8과 10이다.
1과 4는 거리가 차이가 3이고, 4와 8은 차이가 4이지만, 8과 10의 차이는 2로 최솟값이다.
"""

import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev: int = -sys.maxsize
    result: int = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


if __name__ == '__main__':
    print(Solution().minDiffInBST(TreeNode(10, TreeNode(4, TreeNode(1), TreeNode(8)), TreeNode(15))))
