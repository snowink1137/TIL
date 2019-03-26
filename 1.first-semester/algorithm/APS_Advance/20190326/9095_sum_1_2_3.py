import sys

sys.stdin = open('9095.txt', 'r')

memo = [0] * 12
memo[1] = 1
memo[2] = 2
memo[3] = 4

for i in range(4, 12):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(memo[N])
