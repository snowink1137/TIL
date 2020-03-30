import sys
from collections import deque

sys.stdin = open('5250.txt', 'r')

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def bfs(x, y):
    queue = deque()
    visit = [[1000 * 2 * N] * N for _ in range(N)]
    queue.append((x, y))
    visit[x][y] = 0

    while len(queue):
        q = queue.popleft()
        for i in range(4):
            new_x = q[0] + dx[i]
            new_y = q[1] + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                difference = matrix[new_x][new_y] - matrix[q[0]][q[1]]
                if difference >= 0:
                    calculation = visit[q[0]][q[1]] + difference + 1
                else:
                    calculation = visit[q[0]][q[1]] + 1
                if calculation < visit[new_x][new_y]:
                    visit[new_x][new_y] = calculation
                    queue.append((new_x, new_y))

    return visit[N-1][N-1]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = bfs(0, 0)
    print('#{} {}'.format(test_case, result))
