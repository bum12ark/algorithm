"""
* 이진 탐색 트리 (BST)를 더 큰 수 합계 트리로
BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라.
- Example 1
Input : [4, 1, 6, 0, 2, 5, 6, null, null, null, 3, null, null, null, 8]
       4
     /   \
    1     6
   / \   / \
  0   2 5   7
       \     \
        3     8
Output : [30, 36, 21, 36, 35, 26, 16, null, null, null, 33, null, null, null, 8]
       30
     /   \
    36    21
   / \    / \
  36 35  26 15
       \     \
       33     8
Explanation : 자신보다 더 큰 값을 가진 모든 노드의 합이 출력이 된다.
              6의 경우 더 큰 값을 지닌 노드는 7, 8이며 이 값을 모두 합한 6+7+8=21이 출력 노드가 된다.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.bstToGst(root.right)
        self.val += root.right.val
        root.val = self.val
        self.bstToGst(root.left)