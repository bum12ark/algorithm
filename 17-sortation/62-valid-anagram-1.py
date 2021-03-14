"""
* 유효한 애너그램
t가 s의 애너그램인지 판별하라.
- Example 1
Input: s = "anagram", t = nagaram"
Output: true
- Example 2
Input: s = "rat", t = "car'
Ouutput: false
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))