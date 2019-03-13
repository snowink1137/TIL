import sys

sys.stdin = open('2606.txt')


def dfs(v):
    global cnt

    if v == [] or visit[v]:
        return

    visit[v] = True
    cnt += 1

    for i in G[v]:
        dfs(i)


N = int(input())
M = int(input())

G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())

    G[u].append(v)
    G[v].append(u)

visit = [False for _ in range(N+1)]
cnt = -1
dfs(1)
print(cnt)
