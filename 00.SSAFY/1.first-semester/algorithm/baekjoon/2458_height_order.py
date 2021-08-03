import sys

sys.stdin = open('2458.txt', 'r')


def dfs(v):
    global cnt
    if v == [] or visit[v]:
        return

    visit[v] = True
    cnt += 1
    for i in G[v]:
        dfs(i)


def reversed_dfs(v):
    global reversed_cnt
    if v == [] or reversed_visit[v]:
        return

    reversed_visit[v] = True
    reversed_cnt += 1
    for i in reversed_G[v]:
        reversed_dfs(i)


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
reversed_G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    reversed_G[v].append(u)

global_cnt = 0
for i in range(1, N+1):
    visit = [False for _ in range(N+1)]
    cnt = -1
    reversed_visit = [False for _ in range(N+1)]
    reversed_cnt = -1
    dfs(i)
    reversed_dfs(i)
    if cnt + reversed_cnt == N - 1:
        global_cnt += 1

print(global_cnt)
