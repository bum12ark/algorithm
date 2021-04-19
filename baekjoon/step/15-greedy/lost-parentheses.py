"""
출처: https://www.acmicpc.net/problem/1541
"""

# param
s = input().split("-")

# solution
result = 0
for plus_val in s[0].split("+"):
    result += int(plus_val)

for m in s[1:]:
    for minus_val in m.split("+"):
        result -= int(minus_val)

# result
print(result)
