import sys
from collections import deque

sys.stdin = open('1953_sample_input.txt', 'r')

tunnel_differential = [
    [],
    [(-1, 0), (1, 0), (0, -1), (0, 1)],
    [(-1, 0), (1, 0)],
    [(0, -1), (0, 1)],
    [(-1, 0), (0, 1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)],
    [(-1, 0), (0, -1)],
]

T = int(input())
for test_case in range(1, T+1):
    result = 0
    N, M, R, C, L = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]

    visit = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((R, C))
    visit[R][C] += 1
    result += 1
    while q:
        x, y = q.popleft()
        for dx, dy in tunnel_differential[tunnel_map[x][y]]:
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x <= N-1) or not(0 <= new_y <= M-1):
                continue

            if (-dx, -dy) in tunnel_differential[tunnel_map[new_x][new_y]]:
                if not visit[new_x][new_y] and tunnel_map[new_x][new_y]:
                    visit[new_x][new_y] = visit[x][y] + 1
                    if visit[new_x][new_y] <= L:
                        result += 1
                        q.append((new_x, new_y))

    print('#{} {}'.format(test_case, result))
