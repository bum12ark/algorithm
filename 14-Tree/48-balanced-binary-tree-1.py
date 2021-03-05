"""
* 균형 이진 트리
이진 트리가 높이 균형인지 판단하라.
높이 균형은 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것을 말한다.
- Example 1
Input : [3, 9, 20, null, null, 15, 7]
Output : true
     3
   /   \
  9     20
       / \
      15  7
서브 트리 간 높이 차이가 1 이하이므로 높이 균형이다. 따라서 true를 리턴한다.
- Example 2
Input : [1, 2, 2, 3, 3, null, null, 4, 4]
Output : false
       1
     /   \
    2     2
   / \
  3   3
 / \
4   4
1의 왼쪽 서브트리 2와 오른쪽의 2는 높이 차이가 2다. 따라서 false를 리턴한다.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node: TreeNode):
            if not node:
                return 0

            left = check(node.left)
            right = check(node.right)

            return max(left, right)

        check(root)

if __name__ == '__main__':
    param1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    param2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))

    print(Solution().isBalanced(param1))