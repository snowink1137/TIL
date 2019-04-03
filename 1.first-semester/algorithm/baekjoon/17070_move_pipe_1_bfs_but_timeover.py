import sys
from collections import deque

sys.stdin = open('17070.txt', 'r')

dx = (0, 1, 1)
dy = (1, 1, 0)
directions = (1, 2, 3)


def bfs(x, y, direction):
    global result

    queue = deque()
    # visit = [[False] * N for _ in range(N)]
    # visit[x][y] = True
    queue.append((x, y, direction))

    while len(queue):
        q = queue.popleft()

        if (q[0] == N-1) and (q[1] == N-1):
            result += 1
            continue

        if q[2] == 1:
            for i in range(2):
                new_x = q[0] + dx[i]
                new_y = q[1] + dy[i]
                new_direction = directions[i]

                if 0 <= new_x <= N-1 and 0 <= new_y <= N-1:
                    if new_direction == 1:
                        if matrix[new_x][new_y] == 0:
                            queue.append((new_x, new_y, new_direction))
                    elif new_direction == 2:
                        if matrix[new_x][new_y] == 0 and matrix[new_x][new_y-1] == 0 and matrix[new_x-1][new_y] == 0:
                            queue.append((new_x, new_y, new_direction))
        elif q[2] == 2:
            for i in range(3):
                new_x = q[0] + dx[i]
                new_y = q[1] + dy[i]
                new_direction = directions[i]

                if 0 <= new_x <= N-1 and 0 <= new_y <= N-1:
                    if new_direction == 1:
                        if matrix[new_x][new_y] == 0:
                            queue.append((new_x, new_y, new_direction))
                    elif new_direction == 2:
                        if matrix[new_x][new_y] == 0 and matrix[new_x][new_y-1] == 0 and matrix[new_x-1][new_y] == 0:
                            queue.append((new_x, new_y, new_direction))
                    elif new_direction == 3:
                        if matrix[new_x][new_y] == 0:
                            queue.append((new_x, new_y, new_direction))
        elif q[2] == 3:
            for i in range(1, 3):
                new_x = q[0] + dx[i]
                new_y = q[1] + dy[i]
                new_direction = directions[i]

                if 0 <= new_x <= N-1 and 0 <= new_y <= N-1:
                    if new_direction == 3:
                        if matrix[new_x][new_y] == 0:
                            queue.append((new_x, new_y, new_direction))
                    elif new_direction == 2:
                        if matrix[new_x][new_y] == 0 and matrix[new_x][new_y-1] == 0 and matrix[new_x-1][new_y] == 0:
                            queue.append((new_x, new_y, new_direction))


N = int(input())
matrix = []
for _ in range(N):
    matrix.append(tuple(map(int, input().split())))

result = 0
bfs(0, 1, 1)

print(result)
