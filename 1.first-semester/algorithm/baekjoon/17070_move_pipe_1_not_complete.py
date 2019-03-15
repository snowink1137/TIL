import sys
from collections import deque

sys.stdin = open('17070.txt', 'r')

dx = [1, 0, 1]
dy = [1, 1, 0]


def bfs(x, y, direction):
    cnt = 0
    visit[x][y] = True

    queue = deque()

    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x <= N-1 and 0 <= new_y <= N-1:
            if i == 0:
                if matrix[new_x][new_y] == 0 and matrix[new_x-1][new_y] == 0 and matrix[new_x][new_y-1] == 0:
                    queue.append([new_x, new_y, 1])
            else:
                if matrix[new_x][new_y] == 0:
                    queue.append([new_x, new_y, 0])

    while len(queue):
        x, y = queue.popleft()

        if (x == N-1) and (y == N-1):
            cnt += 1
            continue

        if not visit[x][y]:
            visit[x][y] = True

            for i in range(3):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x <= N-1 and 0 <= new_y <= N-1:
                    if i == 0:
                        if matrix[new_x][new_y] == 0 and matrix[new_x-1][new_y] == 0 and matrix[new_x][new_y-1] == 0:
                            if not visit[new_x][new_y]:
                                queue.append([new_x, new_y])
                    else:
                        if matrix[new_x][new_y] == 0:
                            if not visit[new_x][new_y]:
                                queue.append([new_x, new_y])

    return cnt


N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visit = [[False] * N for _ in range(N)]
result = bfs(0, 1, 0)

print(result)
