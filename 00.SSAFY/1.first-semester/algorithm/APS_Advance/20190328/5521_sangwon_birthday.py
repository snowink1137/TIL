import sys
from collections import deque

sys.stdin = open('5521.txt', 'r')


def bfs(v):
    global result

    q = deque()
    visit = [False] * (N + 1)
    D = [0] * (N + 1)

    visit[v] = True
    for friend in G[v]:
        q.append(friend)
        visit[friend] = True
        D[friend] = 1

    while len(q):
        new_v = q.popleft()
        if D[new_v] > 2:
            return

        result += 1

        for new_friend in G[new_v]:
            if not visit[new_friend]:
                q.append(new_friend)
                visit[new_friend] = True
                D[new_friend] = D[new_v] + 1


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    result = 0
    bfs(1)
    print('#{} {}'.format(test_case, result))