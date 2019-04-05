import sys

sys.stdin = open('17070.txt', 'r')

dx = (0, 1, 1)
dy = (1, 1, 0)
directions = (1, 2, 3)

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(tuple(map(int, input().split())))

memo = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
memo[0][1][0] = 1
memo[0][1][1] = 0
memo[0][1][2] = 0

for i in range(N):
    for j in range(1, N):
        pre0_x = i
        pre0_y = j - 1
        if 0 <= pre0_x <= N-1 and 1 <= pre0_y <= N-1:
            if matrix[i][j] == 0:
                memo[i][j][0] += memo[pre0_x][pre0_y][0] + memo[pre0_x][pre0_y][1]

        pre1_x = i - 1
        pre1_y = j - 1
        if 0 <= pre1_x <= N-1 and 1 <= pre1_y <= N-1:
            if matrix[i][j] == 0:
                if matrix[i-1][j] == 0 and matrix[i][j-1] == 0:
                    memo[i][j][1] += memo[pre1_x][pre1_y][0] + memo[pre1_x][pre1_y][1] + memo[pre1_x][pre1_y][2]

        pre2_x = i - 1
        pre2_y = j
        if 0 <= pre2_x <= N-1 and 1 <= pre2_y <= N-1:
            if matrix[i][j] == 0:
                memo[i][j][2] += memo[pre2_x][pre2_y][2] + memo[pre2_x][pre2_y][1]


result = memo[-1][-1][0] + memo[-1][-1][1] + memo[-1][-1][2]
print(result)
