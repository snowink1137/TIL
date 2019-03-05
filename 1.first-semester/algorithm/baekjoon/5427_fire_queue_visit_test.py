import sys
from queue import Queue

sys.stdin = open('F.in', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []
    for _ in range(M):
        matrix.append(list(input()))

    result = 'IMPOSSIBLE'
    visit = [[False] * N for _ in range(M)]
    visit_fire = [[False] * N for _ in range(M)]
    difference = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    start = []
    Q2 = Queue()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == '@':
                start.append(i)
                start.append(j)
                visit[start[0]][start[1]] = True
            elif matrix[i][j] == '*':
                Q2.put([i, j])
                visit_fire[i][j] = True
            elif matrix[i][j] == '#':
                visit[i][j] = True
                visit_fire[i][j] = True

    if start[0] == 0 or start[0] == M - 1 or start[1] == 0 or start[1] == N - 1:
        result = 1
        print('{}'.format(result))
        continue

    Q = Queue()
    Q.put(start)
    flag = False
    cnt = 1
    while not Q.empty():
        cnt += 1
        q2_length = Q2.qsize()
        directions = []
        for _ in range(q2_length):
            v = Q2.get()
            for i in difference:
                new_fire_x = v[0] + i[0]
                new_fire_y = v[1] + i[1]
                if 0 <= new_fire_x < M and 0 <= new_fire_y < N:
                    if not visit_fire[new_fire_x][new_fire_y]:
                        visit_fire[new_fire_x][new_fire_y] = True
                        directions.append([new_fire_x, new_fire_y])

        for w in directions:
            visit_fire[w[0]][w[1]] = True
            Q2.put([w[0], w[1]])

        q_length = Q.qsize()
        directions = []
        for _ in range(q_length):
            v = Q.get()
            for i in difference:
                new_x = v[0] + i[0]
                new_y = v[1] + i[1]
                if 0 <= new_x < M and 0 <= new_y < N:
                    if not visit[new_x][new_y] and not visit_fire[new_x][new_y]:
                        directions.append([new_x, new_y])

        for w in directions:
            if w[0] == 0 or w[0] == M-1 or w[1] == 0 or w[1] == N-1:
                result = cnt
                flag = True
                break

            visit[w[0]][w[1]] = True
            Q.put([w[0], w[1]])

        if flag:
            break

    print('{}'.format(result))
