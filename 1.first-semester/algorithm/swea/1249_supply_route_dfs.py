import sys
from collections import deque

sys.stdin = open('1249.txt', 'r')

dx = (0, 1, 0, 1)
dy = (1, 0, 1, 0)


def dfs(x, y, acc):
    global result

    if visit[x][y]:
        return

    if x == N-1 and y == N-1:
        if acc < result:
            result = acc

        return

    if acc > result:
        return

    visit[x][y] = True
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < N:
            dfs(new_x, new_y, acc+matrix[new_x][new_y])

    visit[x][y] = False


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]

    result = 0xfffffffffffff
    dfs(0, 0, matrix[0][0])

    print('#{} {}'.format(test_case, result))
