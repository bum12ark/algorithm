"""
* 괄호를 삽입하는 여러 가지 방법
숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라.
- Example 1
Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
- Example 2
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def comput(left, right, v):
            ret_val = eval(str(left) + v + str(right))
            return ret_val

        if expression.isdigit():
            return [int(expression)]

        result = []
        for i, v in enumerate(expression):
            if v in "+-*":
                print("left :", expression[:i])
                print("right :", expression[i + 1:])
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                result.append(comput(left, right, v))
        return result


if __name__ == '__main__':
    test_1 = "2-1-1"
    Solution().diffWaysToCompute(test_1)