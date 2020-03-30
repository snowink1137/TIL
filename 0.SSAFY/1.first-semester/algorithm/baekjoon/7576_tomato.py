import sys
from collections import deque

sys.stdin = open('7576.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(check):
    queue = deque()
    D = [[0] * N for _ in range(M)]

    for i in range(len(check)):
        visit[check[i][0]][check[i][1]] = True

        for j in range(4):
            new_x = check[i][0] + dx[j]
            new_y = check[i][1] + dy[j]

            if 0 <= new_x <= M-1 and 0 <= new_y <= N-1:
                if matrix[new_x][new_y] == 0:
                    queue.append([new_x, new_y])
                    D[new_x][new_y] = 1

    while len(queue):
        x, y = queue.popleft()

        if not visit[x][y]:
            visit[x][y] = True

            for j in range(4):
                new_x = x + dx[j]
                new_y = y + dy[j]

                if 0 <= new_x <= M-1 and 0 <= new_y <= N-1 and not visit[new_x][new_y]:
                    if matrix[new_x][new_y] == 0:
                        queue.append([new_x, new_y])
                        if not D[new_x][new_y]:
                            D[new_x][new_y] = D[x][y] + 1

    if sum([sum(x) for x in visit]) == M * N:
        return max([max(x) for x in D])
    else:
        return -1


N, M = map(int, input().split())

matrix = []
for i in range(M):
    matrix.append(list(map(int, input().split())))

visit = [[False] * N for _ in range(M)]
check = []
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 1:
            check.append([i, j])
        elif matrix[i][j] == -1:
            visit[i][j] = True

result = bfs(check)
print(result)
