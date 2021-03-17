"""
전위 순회
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversals:
    # 전위 순회
    def NLR(self, root: TreeNode):
        if not root:
            return
        print(root.val, end='->')
        self.NLR(root.left)
        self.NLR(root.right)

    # 중위 순회
    def LNR(self, root: TreeNode):
        if not root:
            return
        self.LNR(root.left)
        print(root.val, end='->')
        self.LNR(root.right)

    # 후위 순회
    def LRN(self, root: TreeNode):
        if not root:
            return
        self.LRN(root.left)
        self.LRN(root.right)
        print(root.val, end='->')


if __name__ == '__main__':
    param = TreeNode('F',
                     TreeNode('B',
                              TreeNode('A'),
                              TreeNode('D',
                                       TreeNode('C'), TreeNode('E'))
                              ),
                     TreeNode('G',
                              None,
                              TreeNode('I',
                                       TreeNode('H'), None)
                              )
                     )
    TreeTraversals().NLR(param)
    print("\n")
    TreeTraversals().LNR(param)
    print("\n")
    TreeTraversals().LRN(param)
