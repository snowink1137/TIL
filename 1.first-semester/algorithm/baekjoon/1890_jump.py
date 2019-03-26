import sys

sys.stdin = open('1890.txt', 'r')

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
memo = [[0] * N for _ in range(N)]
memo[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break

        capa = matrix[i][j]

        x = i + capa
        y = j + capa

        if 0 <= x < N:
            memo[x][j] += memo[i][j]

        if 0 <= y < N:
            memo[i][y] += memo[i][j]

print(memo[N-1][N-1])
