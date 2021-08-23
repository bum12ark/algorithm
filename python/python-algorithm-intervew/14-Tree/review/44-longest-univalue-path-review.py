"""
url: https://leetcode.com/problems/longest-univalue-path/
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
        def DFS(node):
            if not node:
                return 0

            left = DFS(node.left)
            right = DFS(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0

            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            # 거리를 계산하기 위해 + 연산
            self.result = max(self.result, left + right)

            # 상태 값은 둘 중 더 큰 것을 리턴
            return max(left, right)

        DFS(root)

        return self.result


if __name__ == '__main__':
    # print(Solution().longestUnivaluePath(
    #     TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))),
    #     "||",
    #     2
    # )
    print(Solution().longestUnivaluePath(
        TreeNode(4, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(4))),
        "||",
        3
    )
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[✓] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""