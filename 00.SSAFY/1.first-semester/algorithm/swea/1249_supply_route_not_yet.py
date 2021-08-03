import sys

sys.stdin = open('1249.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]

    dp[0][0] = matrix[0][0]

    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
        dp[j][0] = dp[j-1][0] + matrix[j][0]

    for i in range(1, N):
        for j in range(1, N):
            up = dp[i][j-1]
            left = dp[i-1][j]

            if up > left:
                dp[i][j] = left + matrix[i][j]
            else:
                dp[i][j] = up + matrix[i][j]

    print('#{} {}'.format(test_case, dp[N-1][N-1]))
