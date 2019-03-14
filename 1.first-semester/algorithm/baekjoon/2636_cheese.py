import sys
from collections import deque

sys.stdin = open('2636.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True
    queue = deque()

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (0 <= new_x <= N-1) and (0 <= new_y <= M-1):
            queue.append([new_x, new_y])

    while len(queue):
        queue_x, queue_y = queue.popleft()

        if not visit[queue_x][queue_y]:
            visit[queue_x][queue_y] = True

            if matrix[queue_x][queue_y] == 1:
                matrix[queue_x][queue_y] = 0
            else:
                for i in range(4):
                    new_x = queue_x + dx[i]
                    new_y = queue_y + dy[i]
                    if (0 <= new_x <= N-1) and (0 <= new_y <= M-1):
                        queue.append([new_x, new_y])


N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

pre = 0
for line in matrix:
    pre += sum(line)

if pre == 0:
    cnt = 0
else:
    cnt = 0
    while True:
        bfs(0, 0)
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
