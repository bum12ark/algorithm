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
        def comput(left, right, operater):
            ret = []
            for l in left:
                for r in right:
                    ret.append(eval(str(l) + operater + str(r)))
            return ret

        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, value in enumerate(expression):
            if value in "+-*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                results.extend(comput(left, right, value))
        return results


if __name__ == '__main__':
    test_1 = "2-1-1"
    print(Solution().diffWaysToCompute(test_1))
