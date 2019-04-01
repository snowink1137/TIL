import sys
from collections import deque

sys.stdin = open('5247.txt', 'r')


operation = (1, 1, 2, 10)


def bfs(v):
    q = deque()
    visit = [0] * (M+1) * 2
    visit[v] = 1

    for i in range(len(operation)):
        if i == 0:
            new_v = v + operation[i]
        elif i == 1:
            new_v = v - operation[i]
        elif i == 2:
            new_v = v * operation[i]
        elif i == 3:
            new_v = v - operation[i]
        elif i == 4:
            new_v = v - operation[i]

        if 0 <= new_v < 2 * M:
            q.append(new_v)
            visit[new_v] = 1

            if new_v == M:
                return visit[new_v]

    while len(q):
        qq = q.popleft()

        for i in range(len(operation)):
            if i == 0:
                new_v = qq + operation[i]
            elif i == 1:
                new_v = qq - operation[i]
            elif i == 2:
                new_v = qq * operation[i]
            elif i == 3:
                new_v = qq - operation[i]
            elif i == 4:
                new_v = qq - operation[i]

            if 0 <= new_v < 2*M and not visit[new_v]:
                q.append(new_v)
                visit[new_v] = visit[qq] + 1

                if new_v == M:
                    return visit[new_v]


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'.format(test_case, bfs(N)))
