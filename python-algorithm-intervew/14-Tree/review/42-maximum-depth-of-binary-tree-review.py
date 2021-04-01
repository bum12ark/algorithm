"""
url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
* 이진 트리의 최대 깊이
이진 트리의 최대 깊이를 구하라.
[3, 9, 20, null, null, 15, 7]가 주어졌을 때,
      3
   9    20
      15   7
깊이는 3이다.
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Soution:
    def maxDepth(self, root: TreeNode) -> int:
        Q = collections.deque([root])
        depth = 0

        while Q:
            depth += 1
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return depth


if __name__ == '__main__':
    print(Soution().maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))), 3)
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