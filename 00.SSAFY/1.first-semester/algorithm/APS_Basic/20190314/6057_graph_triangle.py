import sys

sys.stdin = open('6057.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    combinations = []
    vertexes = [x for x in range(1, N)]

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                combinations.append([i, j, k])

    cnt = 0
    for i in range(len(combinations)):
        if (combinations[i][1] in G[combinations[i][0]]) and (combinations[i][2] in G[combinations[i][1]]) and (combinations[i][0] in G[combinations[i][2]]):
            cnt += 1

    print('#{} {}'.format(test_case, cnt))
