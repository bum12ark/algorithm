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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

if __name__ == '__main__':
    param = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(Solution().rangeSumBST(param, 7, 15))