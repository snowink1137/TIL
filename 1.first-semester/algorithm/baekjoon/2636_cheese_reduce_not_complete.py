import sys

sys.stdin = open('2636.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    if visit[x][y]:
        return

    if matrix[x][y] == 0:
        visit[x][y] = True

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < M and 0 <= new_y < N:
                dfs(new_x, new_y)
    else:
        matrix[x][y] = 0
        visit[x][y] = True


N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

pre = 0
for line in matrix:
    pre += sum(line)

cnt = 0
while True:
    visit = [[False] * M for _ in range(N)]
    dfs(0, 0)
    matrix_sum = 0
    for line in matrix:
        matrix_sum += sum(line)

    if matrix_sum == 0:
        cnt += 1
        break
    else:
        cnt += 1
        pre = matrix_sum

print(cnt)
print(pre)
