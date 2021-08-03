import sys
from collections import deque

sys.stdin = open('1249.txt', 'r')

dx = (0, 1, 0, 1)
dy = (1, 0, 1, 0)


def bfs(x, y):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    Q = deque()
    visit[x][y] = matrix[x][y]
    Q.append((x, y))

    while len(Q):
        q = Q.popleft()

        for i in range(4):
            new_x = q[0] + dx[i]
            new_y = q[1] + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                temp = visit[q[0]][q[1]] + matrix[new_x][new_y]
                if visit[new_x][new_y] == 0:
                    visit[new_x][new_y] = temp
                    Q.append((new_x, new_y))
                elif temp < visit[new_x][new_y]:
                    visit[new_x][new_y] = temp
                    Q.append((new_x, new_y))

    return visit[N-1][N-1]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    result = bfs(0, 0)
    print('#{} {}'.format(test_case, result))
