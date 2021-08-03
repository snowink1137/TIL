import sys
from collections import deque

sys.stdin = open('2589.txt', 'r')


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    visit = [[False] * M for _ in range(N)]
    D = [[0] * M for _ in range(N)]
    queue = deque()

    visit[x][y] = True
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x <= N-1 and 0 <= new_y <= M-1:
            if matrix[new_x][new_y] == 'L':
                queue.append([new_x, new_y])
                D[new_x][new_y] = D[x][y] + 1

    while len(queue):
        queue_x, queue_y = queue.popleft()

        if not visit[queue_x][queue_y]:
            visit[queue_x][queue_y] = True

            for i in range(4):
                new_x = queue_x + dx[i]
                new_y = queue_y + dy[i]
                if 0 <= new_x <= N - 1 and 0 <= new_y <= M - 1:
                    if not visit[new_x][new_y]:
                        if matrix[new_x][new_y] == 'L':
                            queue.append([new_x, new_y])
                            D[new_x][new_y] = D[queue_x][queue_y] + 1

    temp = [max(x) for x in D]
    return max(temp)


N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(input()))

max_time = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            temp = bfs(i, j)
            if temp > max_time:
                max_time = temp

print(max_time)
