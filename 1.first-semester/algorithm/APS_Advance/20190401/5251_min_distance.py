import sys

sys.stdin = open('5251.txt', 'r')


def dijkstra(G, s, e):
    D = [11] * (N + 1)
    P = [None] * (N + 1)
    visit = [False] * (N + 1)
    D[s] = 0

    for _ in range(N+1):
        min_index = -1
        min_weight = 11
        for i in range(N+1):
            if not visit[i] and D[i] < min_weight:
                min_weight = D[i]
                min_index = i

        visit[min_index] = True
        for v, weight in G[min_index]:
            if not visit[v] and D[min_index] + weight < D[v]:
                D[v] = D[min_index] + weight
                P[v] = min_index

    return D[e]

T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))

    result = dijkstra(G, 0, N)
    print('#{} {}'.format(test_case, result))
