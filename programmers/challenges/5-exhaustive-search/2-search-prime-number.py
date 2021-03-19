"""
* 소수 찾기
한자리 숫자가 적힌 종이 조각이 흩어져있습니다.
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
- Example 1
Input: "17"
Output: 3
- Example 2
Input: "011"
Output: 2

입출력 예 설명
- 예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
- 예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
11과 011은 같은 숫자로 취급합니다.
"""
import math
from typing import List

result: List[int] = []
prev_element = []
def solution(numbers: str) -> int:
    def check(n):
        k = math.sqrt(n)
        if n < 2:
            return False

        for i in range(2, int(k) + 1):
            if n % i == 0:
                return False
        return True

    def permutation(nums: List[str]):
        if prev_element:
            prev_val = int(''.join(prev_element))
            if check(int(prev_val)):
                result.append(prev_val)

        if not nums:
            return

        for idx, value in enumerate(nums):
            next_element = nums[:]
            prev_element.append(value)
            del next_element[idx]
            permutation(next_element)
            prev_element.pop()

    permutation(list(numbers))
    print(result)
    return len(set(result))


print(solution("011"))