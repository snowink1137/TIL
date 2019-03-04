import sys
from queue import Queue
from collections import deque

sys.stdin = open('1238_input.txt', 'r')


def bfs(s):
    visit = [False] * (N+1)
    D = [0] * (N+1)

    # Q = Queue()
    # Q.put(s)
    Q = deque()
    Q.append(s)
    visit[s] = True

    while not len(Q) == 0:
        # v = Q.get()
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                visit[w] = True
                # Q.put(w)
                Q.append(w)


    longest = max(D)
    long_list = []
    for idx in range(N+1):
        if D[idx] == longest:
            long_list.append(idx)

    return max(long_list)


for test_case in range(1, 11):
    N, s = map(int, input().split())

    information = list(map(int, input().split()))

    G = [[] for _ in range(N+1)]
    for i in range(0, N, 2):
        G[information[i]].append(information[i+1])

    result = bfs(s)
    print('#{} {}'.format(test_case, result))
