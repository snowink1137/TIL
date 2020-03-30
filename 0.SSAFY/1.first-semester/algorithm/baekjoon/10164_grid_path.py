import sys

sys.stdin = open('10164.txt', 'r')

N, M, K = map(int, input().split())

if K == 0:
    x = 0
    y = 0
else:
    x = (K-1) // M
    y = (K-1) % M

matrix = [[0] * M for _ in range(N)]
matrix[0][0] = 1

for i in range(N):
    for j in range(M):
        if 0 <= i-1 < N and 0 <= j-1 < M:
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        elif 0 <= i-1 < N:
            matrix[i][j] = matrix[i-1][j]
        elif 0 <= j-1 < M:
            matrix[i][j] = matrix[i][j-1]

print(matrix[x][y] * matrix[N-x-1][M-y-1])
