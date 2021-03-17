"""
* 이진 트리 반전
- Exmaple 1
Input :
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output :
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inverTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.inverTree(root.right), self.inverTree(root.left)
            return root