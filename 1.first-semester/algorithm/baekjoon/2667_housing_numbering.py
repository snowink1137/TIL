import sys

sys.stdin = open('2667.txt', 'r')


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    global cnt, cnt_inside
    if visit[x][y] or matrix[x][y] == 0:
        return

    visit[x][y] = True
    cnt_inside += 1

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < N:
            dfs(new_x, new_y)


N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

visit = [[False] * N for _ in range(N)]
cnt = 0
cnt_list = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0 and not visit[i][j]:
            cnt_inside = 0
            dfs(i, j)
            cnt_list.append(cnt_inside)
            cnt += 1

print(cnt)
cnt_list.sort()
for i in range(cnt):
    print(cnt_list[i])
