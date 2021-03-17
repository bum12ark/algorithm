"""
* 이진 트리의 직경
이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.
이진 트리가 주어졌을 때,
          1
         / \
        2   3
       / \
      4   5
가장 긴 경로는 4->2->1->3 또는 5->2->1->3 으로 3이다.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 리프 노드까지 탐색한 다음 부모로 거슬러 올라가면서 각각의 거리를 계산
        def dfs(node: TreeNode):
            # 리프 노드가 없을 경우 -1 리턴
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest

if __name__ == '__main__':
    solution = Solution()
    print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))