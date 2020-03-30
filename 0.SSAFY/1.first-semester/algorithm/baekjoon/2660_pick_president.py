import sys
from collections import deque

sys.stdin = open('2660.txt', 'r')


def bfs(v):
    visit = [False for _ in range(N+1)]
    D = [0 for _ in range(N+1)]
    queue = deque()

    visit[v] = True
    for i in G[v]:
        queue.append(i)
        D[i] = D[v] + 1

    while len(queue):
        v = queue.popleft()

        if not visit[v]:
            visit[v] = True

            for s in G[v]:
                if not visit[s]:
                    queue.append(s)
                    if not D[s]:
                        D[s] = D[v] + 1

    return max(D[1:])


N = int(input())

G = [[] for _ in range(N+1)]
a, b = map(int, input().split())

while a != -1:
    G[a].append(b)
    G[b].append(a)

    a, b = map(int, input().split())

score_list = []
for i in range(1, N+1):
    score_list.append(bfs(i))

min_score = min(score_list)
candidates = []
cnt = 0
for i in range(len(score_list)):
    if score_list[i] == min_score:
        candidates.append(i+1)
        cnt += 1

candidates.sort()
print('{} {}'.format(min_score, cnt))
print(' '.join(map(str, candidates)))
