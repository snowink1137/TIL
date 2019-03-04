import sys
from queue import Queue

sys.stdin = open('5105_sample_input.txt', 'r')


def bfs(s):
    global result
    visit = [[False] * N for i in range(N)]
    D = [[0] * N for i in range(N)]

    Q = Queue()
    Q.put(s)
    visit[s[0]][s[1]] = True
    while not Q.empty():
        v = Q.get()
        difference = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        directions = []
        for i in difference:
            new_x = v[0] + i[0]
            new_y = v[1] + i[1]
            if 0 <= new_x < N and 0 <= new_y < N:
                if matrix[new_x][new_y] == 0 or matrix[new_x][new_y] == 2 or matrix[new_x][new_y] == 3:
                    directions.append([new_x, new_y])

        for w in directions:
            if not visit[w[0]][w[1]]:
                D[w[0]][w[1]] = D[v[0]][v[1]] + 1
                visit[w[0]][w[1]] = True
                Q.put(w)
            if matrix[w[0]][w[1]] == 3:
                result = D[w[0]][w[1]] - 1
                return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input())))

    start = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start.append(i)
                start.append(j)
                break

    result = 0
    bfs(start)
    print('#{} {}'.format(test_case, result))
