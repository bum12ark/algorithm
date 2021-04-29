"""
출처: https://www.acmicpc.net/problem/10816
"""
import collections
import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

counter = collections.Counter(N_list)

for m in M_list:
    print(counter[m], end=" ")
