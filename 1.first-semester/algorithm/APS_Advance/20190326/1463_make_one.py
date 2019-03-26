import sys

sys.stdin = open('1463.txt', 'r')


N = int(input())
memo = [0] * (N+1)
memo[1] = 0
if N == 1:
    print(memo[N])
elif N <= 2:
    memo[2] = 1
    print(memo[N])
elif 2 < N <= 3:
    memo[2] = 1
    memo[3] = 1
    print(memo[N])
else:
    memo[2] = 1
    memo[3] = 1
    for i in range(4, N+1):
        if not i % 2 and not i % 3:
            memo[i] = min(memo[i//2], memo[i//3], memo[i-1]) + 1
        elif not i % 2:
            memo[i] = min(memo[i//2], memo[i-1]) + 1
        elif not i % 3:
            memo[i] = min(memo[i//3], memo[i-1]) + 1
        else:
            memo[i] = memo[i-1] + 1

    print(memo[N])
