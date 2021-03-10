"""
* 이진 탐색 트리(BST) 합의 범위
이진 탐색 트리(BST)가 주어졌을 때 L 이상 R 이하의 값을 지닌 노드의 합을 구하라.
- Example 1
Input : root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
      10
   /    \
  5      15
 / \      \
3   7     18
Output : 32
Explanation : 7 이상 15 이하인 또 다른 노드는 10이 있으며 따라서 결과는 7 + 10 + 15 = 32가 된다.
"""


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def myRangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        queue, sum = collections.deque([root]), 0

        while queue:
            node = queue.popleft()

            if node:
                if node.val > L:
                    queue.append(node.left)
                if node.val < R:
                    queue.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum

    # 반복 구조 BFS로 필요한 노드 탐색
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        queue, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > L:
                    queue.append(node.left)
                if node.val < R:
                    queue.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum


if __name__ == '__main__':
    param = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(Solution().myRangeSumBST(param, 7, 15))
    print(Solution().rangeSumBST(param, 7, 15))