import sys
from collections import deque

sys.stdin = open('2468.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = deque()
    visit[x][y] = True

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x <= N-1 and 0 <= new_y <= N-1:
            if matrix[new_x][new_y] > k:
                queue.append([new_x, new_y])

    while len(queue):
        x, y = queue.popleft()

        if not visit[x][y]:
            visit[x][y] = True

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x <= N - 1 and 0 <= new_y <= N - 1 and not visit[new_x][new_y]:
                    if matrix[new_x][new_y] > k:
                        queue.append([new_x, new_y])


N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

result = 0
for k in range(101):
    cnt = 0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > k and not visit[i][j]:
                bfs(i, j)
                cnt += 1
            elif matrix[i][j] <= k:
                visit[i][j] = True

    if cnt > result:
        result = cnt

print(result)
