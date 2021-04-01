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
        pass


if __name__ == '__main__':
    head = Solution().inverTree(
        TreeNode(4,
                 TreeNode(2,
                          TreeNode(1),
                          TreeNode(3)
                          ),
                 TreeNode(7,
                          TreeNode(6),
                          TreeNode(9)
                          )
                 )
    )
