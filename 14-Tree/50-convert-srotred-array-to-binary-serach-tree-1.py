"""
* 정렬된 배열의 이진 탐색 트리 변환
오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.
- Example 1
Input : nums = [-10, -3, 0, 5, 9]
Output :
       0
     /   \
    -3   9
   /    /
 -10   5

      0
    /   \
   -10   5
      \   \
      -3   9
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

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

if __name__ == '__main__':
    result = Solution().sortedArrayToBST([-10, -7, -3, 0, 5, 7, 9])
    print(Solution().serialize(result))