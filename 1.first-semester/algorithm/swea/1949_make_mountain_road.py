import sys

sys.stdin = open('1949.txt', 'r')

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def dfs(x, y, cnt, use):
    global result

    if visit[x][y]:
        if cnt-1 > result:
            result = cnt-1
        return

    visit[x][y] = True
    flag = False
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < N:
            if matrix[x][y] > matrix[new_x][new_y]:
                dfs(new_x, new_y, cnt+1, use)
                flag = True
            else:
                if not use and (matrix[x][y] > matrix[new_x][new_y] - K):
                    temp = matrix[new_x][new_y]
                    matrix[new_x][new_y] = matrix[x][y] - 1
                    dfs(new_x, new_y, cnt+1, True)
                    flag = True
                    matrix[new_x][new_y] = temp

    if not flag:
        if cnt > result:
            result = cnt

    visit[x][y] = False
    return


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_height = max([max(i) for i in matrix])

    max_height_index = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_height:
                max_height_index.append([i, j])

    result = 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    for index in max_height_index:
        dfs(index[0], index[1], 1, False)

    print('#{} {}'.format(test_case, result))
