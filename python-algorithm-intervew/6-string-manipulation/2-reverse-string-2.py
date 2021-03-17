from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()

if __name__ == '__main__':
    solution = Solution()
    param: List[str] = ["h", "e", "l", "l", "o"]
    solution.reverseString(param)
    print(param)