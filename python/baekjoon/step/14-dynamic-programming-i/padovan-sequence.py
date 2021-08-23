import collections

# param
size = int(input())
case = [int(input()) for _ in range(size)]
dp = collections.defaultdict(int)


# function
def solution(n):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2]

    return dp[n]


# main
if __name__ == '__main__':
    for c in case:
        print(solution(c))