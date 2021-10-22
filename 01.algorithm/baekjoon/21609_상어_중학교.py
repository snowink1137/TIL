import sys

sys.stdin = open('21609_sample_input.txt', 'r')

from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def bfs(i, j, matrix, candidates):
    global N
    group = []
    queue = deque()
    queue.append((i, j))
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[i][j] = True
    group.append((i, j))
    cnt = 1
    rainbow_cnt = 0

    while queue:
        q = queue.pop()
        x, y = q[0], q[1]

        for k in range(4):
            new_x, new_y = x + dx[k], y + dy[k]

            if not (0 <= new_x < N and 0 <= new_y < N) or visit[new_x][new_y]:
                continue

            if matrix[new_x][new_y] != matrix[i][j] and matrix[new_x][new_y] != 0:
                continue

            queue.append((new_x, new_y))
            visit[new_x][new_y] = True
            group.append((new_x, new_y))
            cnt += 1
            if matrix[new_x][new_y] == 0:
                rainbow_cnt += 1

    group.sort(key=lambda x: (x[0], x[1]))
    for g in group:
        if matrix[g[0]][g[1]] != 0:
            standard = g
            break

    candidates.append([cnt, rainbow_cnt, standard[0], standard[1], group])
    return


def check(matrix):
    global N
    candidates = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and matrix[i][j] > 0:
                bfs(i, j, matrix, candidates)
                visit[i][j] = True

    return candidates


def delete(matrix, group):
    cnt = 0
    for g in group:
        matrix[g[0]][g[1]] = -2
        cnt += 1

    return cnt ** 2


def gravity(matrix):
    global N
    for j in range(N):
        for i in range(N-1, 0, -1):
            if matrix[i][j] != -2:
                continue

            for k in range(i-1, -1, -1):
                if matrix[k][j] == -1:
                    break
                elif matrix[k][j] == -2:
                    continue
                else:
                    matrix[i][j], matrix[k][j] = matrix[k][j], matrix[i][j]
                    break

    return


def rotate_reverse_90(matrix):
    return list(map(list, list(zip(*matrix))[::-1]))


while True:
    block_group = check(matrix)
    if len(block_group) < 1:
        break

    block_group.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    if block_group[0][0] < 2:
        break

    answer += delete(matrix, block_group[0][4])

    gravity(matrix)
    matrix = rotate_reverse_90(matrix)
    gravity(matrix)

print(answer)
