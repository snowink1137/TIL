import sys
from collections import deque

sys.stdin = open('F.in', 'r')


difference = [[1, 0], [-1, 0], [0, 1], [0, -1]]
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []
    for _ in range(M):
        matrix.append(list(input()))

    result = 'IMPOSSIBLE'
    visit = [[False] * N for _ in range(M)]
    visit_fire = [[False] * N for _ in range(M)]

    start = []
    Q2 = deque()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == '@':
                start.append(i)
                start.append(j)
                visit[start[0]][start[1]] = True
            elif matrix[i][j] == '*':
                Q2.append([i, j])
                visit_fire[i][j] = True
            elif matrix[i][j] == '#':
                visit[i][j] = True
                visit_fire[i][j] = True

    if start[0] == 0 or start[0] == M - 1 or start[1] == 0 or start[1] == N - 1:
        result = 1
        print(result)
        continue

    Q = deque()
    Q.append(start)
    flag = False
    cnt = 1
    while not len(Q) == 0:
        cnt += 1
        q2_length = len(Q2)
        directions = []
        for _ in range(q2_length):
            v = Q2.popleft()
            for i in difference:
                new_fire_x = v[0] + i[0]
                new_fire_y = v[1] + i[1]
                if 0 <= new_fire_x < M and 0 <= new_fire_y < N and not visit_fire[new_fire_x][new_fire_y]:
                    visit_fire[new_fire_x][new_fire_y] = True
                    directions.append([new_fire_x, new_fire_y])
                    visit_fire[new_fire_x][new_fire_y] = True
                    Q2.append([new_fire_x, new_fire_y])

        q_length = len(Q)
        for _ in range(q_length):
            v = Q.popleft()
            for i in difference:
                new_x = v[0] + i[0]
                new_y = v[1] + i[1]
                if 0 <= new_x < M and 0 <= new_y < N and not visit[new_x][new_y] and not visit_fire[new_x][new_y]:
                    if new_x == 0 or new_x == M-1 or new_y == 0 or new_y == N-1:
                        result = cnt
                        flag = True
                        break
                    visit[new_x][new_y] = True
                    Q.append([new_x, new_y])

            if flag:
                break

        if flag:
            break

    print(result)
