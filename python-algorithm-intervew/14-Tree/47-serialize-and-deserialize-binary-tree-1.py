"""
* 이진 트리 직렬화 & 역직렬화
이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.
즉 다음과 같은 트리는 [1, 2, 3, null, null, 4, 5] 형태로 직렬화할 수 있을 것이다.
     1
   /   \
  2     3
 / \   / \
      4   5
"""

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data: str):
        nodes = data.split(' ')

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])

        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root

if __name__ == '__main__':
    print(Solution().serialize(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))
    d_tree = Solution().deserialize('# 1 2 3 # # 4 5 # # # #')
    print(Solution().serialize(d_tree))
