"""
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
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth

if __name__ == '__main__':
    solution = Soution()
    print(solution.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))))