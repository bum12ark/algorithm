"""
url: https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
* 큰 수 만들기
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
- number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
- k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예
- Example 1
Input: number = "1924", k = 2
Output: "94"
- Example 2
Input: number = "1231234", k = 3
Output: "3234
- Example 3
Input: number = "4177252841", k = 4
Output: "775841
"""


def solution(number: str, k: int) -> str:
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


if __name__ == '__main__':
    print(solution("4321", 2))
