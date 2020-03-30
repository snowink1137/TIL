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
        for w in Graph[v[0]][v[1]]:
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
    Graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            target = matrix[i][j]
            if target == 2:
                start.append(i)
                start.append(j)
                target2 = matrix[i][j + 1]
                if target2 == 0 or target2 == 2 or target2 == 3:
                    Graph[i][j].append([i, j+1])
                    Graph[i][j+1].append([i, j])
            elif target == 1:
                continue
            elif target == 0 or target == 3:
                target2 = matrix[i][j+1]
                if target2 == 0 or target2 == 2 or target2 == 3:
                    Graph[i][j].append([i, j+1])
                    Graph[i][j+1].append([i, j])

    for j in range(N):
        for i in range(N-1):
            target = matrix[i][j]
            if target == 2 or target == 3 or target == 0:
                target2 = matrix[i+1][j]
                if target2 == 2 or target2 == 3 or target2 == 0:
                    Graph[i][j].append([i+1, j])
                    Graph[i+1][j].append(([i, j]))

    result = 0
    bfs(start)
    print('#{} {}'.format(test_case, result))

