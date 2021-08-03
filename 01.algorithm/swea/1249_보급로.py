import sys
from collections import deque

sys.stdin = open('1249_sample_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        q = queue.popleft()
        x = q[0]
        y = q[1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            temp = visit[x][y] + battle_field_map[new_x][new_y]
            if temp < visit[new_x][new_y]:
                visit[new_x][new_y] = temp
                queue.append((new_x, new_y))

    return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    battle_field_map = [[int(i) for i in input()] for _ in range(N)]

    visit = [[9*N*N for _ in range(N)] for _ in range(N)]
    visit[0][0] = 0
    bfs()
    result = visit[N-1][N-1]

    print('#{} {}'.format(test_case, result))
