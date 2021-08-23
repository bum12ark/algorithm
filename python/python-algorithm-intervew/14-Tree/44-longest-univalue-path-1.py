"""
* 가장 긴 동일 값의 경로
동일한 값을 지닌 가장 긴 경로를 찾아라.
- Example 1
Input :
          5
         / \
        4   5
       / \   \
      1   1   5
Output : 2
Explaination : 루트에서 오른쪽 노드 끝까지 5->5->5로 가장 긴 이동 거리가 2이다.
- Example 2
Input :
          1
         / \
        4   5
       / \   \
      4   4   5
Output : 2
Explaination : 왼쪽 리프 노드 4에서 형제 노드 4까지 4->4->4로 가장 긴 이동 거리가 2이다.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))))