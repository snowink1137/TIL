import sys
from itertools import combinations

sys.stdin = open('1767.txt', 'r')

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def dfs(n, combi, visit_k_origin, k=0, acc=0):
    global result

    if k == n:
        if acc < result:
            result = acc

        return

    for i in range(4):
        flag = False
        cnt = 0
        visit_k = [visit_k_origin[i][:] for i in range(N)]
        new_x = not_connect[combi[k]][0] + dx[i]
        new_y = not_connect[combi[k]][1] + dy[i]

        if not (0 <= new_x < N and 0 <= new_y < N):
            continue

        while 0 <= new_x < N and 0 <= new_y < N:
            if visit_k[new_x][new_y] != 0:
                flag = True
                break

            cnt += 1
            visit_k[new_x][new_y] = 2
            new_x += dx[i]
            new_y += dy[i]

        if flag:
            continue

        dfs(n, combi, visit_k, k+1, acc+cnt)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    not_connect = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if matrix[i][j] == 1:
                not_connect.append((i, j))

    connect = []
    for i in [0, N-1]:
        for j in range(N):
            if matrix[i][j] == 1:
                connect.append((i, j))

    for j in [0, N-1]:
        for i in range(1, N-1):
            if matrix[i][j] == 1:
                connect.append((i, j))

    l = len(not_connect)
    for n in range(l, -1, -1):
        result = 0xffffff
        for combi in combinations(range(l), n):
            visit_0_origin = [matrix[i][:] for i in range(N)]
            dfs(n, combi, visit_0_origin)

        if result != 0xffffff:
            break

    print('#{} {}'.format(test_case, result))
