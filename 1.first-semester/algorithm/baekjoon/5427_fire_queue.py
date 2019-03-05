import sys
from queue import Queue

sys.stdin = open('5427.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []
    for _ in range(M):
        matrix.append(list(input()))

    start = []
    fires = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == '@':
                start.append(i)
                start.append(j)
            if matrix[i][j] == '*':
                fires.append([i, j])

    result = 'IMPOSSIBLE'
    visit = [[False] * N for _ in range(M)]
    difference = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    Q = Queue()
    Q.put(start)
    visit[start[0]][start[1]] = True
    flag = False
    cnt = 0
    while not Q.empty():
        cnt += 1
        for fire in fires[:]:
            for i in difference:
                new_fire_x = fire[0] + i[0]
                new_fire_y = fire[1] + i[1]
                if 0 <= new_fire_x < M and 0 <= new_fire_y < N:
                    if matrix[new_fire_x][new_fire_y] != '#':
                        matrix[new_fire_x][new_fire_y] = '*'
                        fires.append([new_fire_x, new_fire_y])

        for _ in range(Q.qsize()):
            v = Q.get()
            visit[v[0]][v[1]] = True
            directions = []
            for i in difference:
                new_x = v[0] + i[0]
                new_y = v[1] + i[1]
                if 0 <= new_x < M and 0 <= new_y < N:
                    if matrix[new_x][new_y] == '.':
                        directions.append([new_x, new_y])

            for w in directions:
                if w[0] == 0 or w[0] == M-1 or w[1] == 0 or w[1] == N-1:
                    result = cnt + 1
                    flag = True
                    break
                if not visit[w[0]][w[1]]:
                    Q.put(w)

            if flag:
                break

        if flag:
            break

    print('#{} {}'.format(test_case, result))
