import sys

sys.stdin = open('5249.txt', 'r')


def mst_prim(G, s):
    key = [11] * (V + 1)
    pi = [None] * (V + 1)
    visit = [False] * (V + 1)
    key[s] = 0

    for _ in range(V+1):
        min_index = -1
        min_weight = 11
        for i in range(V+1):
            if not visit[i] and key[i] < min_weight:
                min_weight = key[i]
                min_index = i

        visit[min_index] = True
        for v, weight in G[min_index]:
            if not visit[v] and weight < key[v]:
                key[v] = weight
                pi[v] = min_index

    return sum(key)


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1].append((n2, w))
        G[n2].append((n1, w))

    result = mst_prim(G, 0)
    print('#{} {}'.format(test_case, result))
