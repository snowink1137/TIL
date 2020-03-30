import sys
from collections import deque

sys.stdin = open('1260.txt', 'r')


def dfs(v):
    if v == 0 or visit_dfs[v]:
        return

    visit_dfs[v] = True
    print(v, end=' ')
    for i in G[v]:
        dfs(i)


def bfs(v):
    visit_bfs[v] = True
    print(v, end=' ')
    for i in G[v]:
        queue.append(i)

    while len(queue):
        q = queue.popleft()
        if not visit_bfs[q]:
            visit_bfs[q] = True
            print(q, end=' ')
            for i in G[q]:
                queue.append(i)


N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
visit_dfs = [0 for _ in range(N+1)]
visit_bfs = [0 for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for info in G:
    info.sort()

queue = deque()
dfs(V)
print()
bfs(V)
