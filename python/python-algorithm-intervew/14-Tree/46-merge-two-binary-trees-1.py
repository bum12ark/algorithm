"""
* 두 이진 트리 병합
두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다.
- Example 1
Input :
     1             2
   /   \         /   \
  3     2       1     3
 /               \     \
5                 4     7
Output :
     3
   /   \
  4     5
 / \     \
5   3     7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            # 둘 중에 None이 아닌 것을 리턴, 둘 다 None일 경우 None 리턴
            return root1 or root2
