import sys

sys.stdin = open('4875_sample_input.txt', 'r')


def dfs(x, y):
    global result
    if result == 1:
        return
    v_x = x
    v_y = y
    visit[v_x][v_y] = True

    if matrix[x][y] == 3:
        result = 1
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        new_x = v_x + dx[i]
        new_y = v_y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N and not visit[new_x][new_y] and (matrix[new_x][new_y] == 0 or matrix[new_x][new_y] == 3):
            dfs(new_x, new_y)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input())))

    start = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start.append(i)
                start.append(j)
                break

    if len(start) != 0:
        stack = [[start[0], start[1]]]
        visit = [[False]*N for _ in range(N)]
        result = 0
        dfs(start[0], start[1])

    print(f'#{test_case} {result}')
