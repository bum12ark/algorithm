"""
url:
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
        def DFS(node):
            # 노드가 없는 경우 1로 초기화
            if not node:
                return 1

            left = DFS(node.left)
            right = DFS(node.right)

            self.longest = max(self.longest, left, right)

            # 두 상태값 중 더 높은것 + 1로 리턴
            return max(left, right) + 1

        DFS(root)

        return self.longest


if __name__ == '__main__':
    print(Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))), "||", 3)
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[] 코드 50% 정도 완성
[✓] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""