import sys
from queue import Queue

sys.stdin = open('5102_sample_input.txt', 'r')


def bfs(S, G):
    visit = [False] * (V + 1)
    D = [0] * (V + 1)

    Q = Queue()
    Q.put(S)
    visit[S] = True
    key = 0
    while not Q.empty():
        v = Q.get()
        for w in Graph[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                visit[w] = True
                Q.put(w)

            if w == G:
                key = w
                break

    return D[key]


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())

    Graph = [[] for _ in range(V + 1)]

    for i in range(E):
        u, v = map(int, input().split())
        Graph[u].append(v)
        Graph[v].append(u)

    S, G = map(int, input().split())

    distance = bfs(S, G)
    print('#{} {}'.format(test_case, distance))
