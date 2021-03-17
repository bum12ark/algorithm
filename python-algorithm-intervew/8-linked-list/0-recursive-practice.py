from typing import List

# 재귀함수를 이용하여 1부터 n까지의 곱셈을 구현하라.
def multiple(num: int) -> int:
    if num == 1:
        return 1
    return num * multiple(num - 1)

# 문제 2) 숫자가 들어있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 구현하라
def total(data_list:List[int]) -> int:
    if len(data_list) <= 1:
        return data_list[0]
    else:
        return data_list[0] + total(data_list[1::])

# 문제 3) 회문(Palindrome)을 판단하는 함수를 재귀용법으로 구현하라
def is_palindrome(word: str) -> bool:
    if len(word) <= 2:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        False
"""
문제 4) 아래의 조건을 기반으로 재귀함수를 이용해 구현하라
a) 정수 n이 있다.
b) n이 홀수이면 → 3 x n + 1 수행
c) n이 짝수이면 → n/2 수행 
d) 이를 반복하여 n이 결국 1이 될 때까지의 과정을 모두 출력하는 재귀함수를 구현하라 
"""
def calculation(num: int) -> int:
    if num == 1:
        return num
    if num % 2 == 0: # 짝수이면
        return calculation(int(num / 2))
    else: # 홀수인 경우
        return calculation(int(3 * num + 1))

"""
문제 5) 아래의 조건을 기반으로 재귀함수를 이용해 구현하라
- 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오
"""
def question5(data: int) -> int:
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return question5(data - 1) + question5(data - 2) + question5(data - 3)

print('multiple : ', multiple(3))
print('total : ', total([1, 2, 3]))
print('is_palindrome : ', is_palindrome("level"))
print('calculation : ', calculation(3))
print('question5 : ', question5(7))