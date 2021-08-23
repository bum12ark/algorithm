"""
출처: https://www.acmicpc.net/problem/1427
"""

if __name__ == '__main__':
    nums = list(map(int, input()))
    nums.sort(reverse=True)
    print(''.join(map(str, nums)))