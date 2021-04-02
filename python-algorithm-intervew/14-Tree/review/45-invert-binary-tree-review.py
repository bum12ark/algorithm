"""
url: https://leetcode.com/problems/invert-binary-tree/
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
    def inverTree_BFS(self, root: TreeNode) -> TreeNode:
        Q = collections.deque([root])

        while Q:
            node = Q.popleft()
            if node:
                node.left, node.right = node.right, node.left

                Q.append(node.left)
                Q.append(node.right)

        return root

    def inverTree_DFS(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root


if __name__ == '__main__':
    head = Solution().inverTree_BFS(
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
