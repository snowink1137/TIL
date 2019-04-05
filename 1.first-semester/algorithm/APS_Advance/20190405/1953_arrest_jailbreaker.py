import sys
from collections import deque

sys.stdin = open('1953.txt', 'r')

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
check_list = [0, [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]], [[1, 2, 5, 6], [1, 2, 4, 7], [], []], [[], [], [1, 3, 4, 5], [1, 3, 6, 7]], [[1, 2, 5, 6], [], [], [1, 3, 6, 7]], [[], [1, 2, 4, 7], [], [1, 3, 6, 7]], [[], [1, 2, 4, 7], [1, 3, 4, 5], []], [[1, 2, 5, 6], [], [1, 3, 4, 5], []]]


def bfs(x, y):
    queue = deque()
    visit = [[0 for _ in range(M)] for _ in range(N)]

    queue.append((x, y))
    visit[x][y] = 1

    while len(queue):
        q = queue.popleft()

        for i in range(4):
            new_x = q[0] + dx[i]
            new_y = q[1] + dy[i]

            if visit[q[0]][q[1]] == L:
                sum_visit = sum([M - i.count(0) for i in visit])
                return sum_visit

            if 0 <= new_x < N and 0 <= new_y < M and not visit[new_x][new_y]:
                if matrix[new_x][new_y]:
                    if matrix[q[0]][q[1]] in check_list[matrix[new_x][new_y]][i]:
                        if not visit[new_x][new_y]:
                            queue.append((new_x, new_y))
                            visit[new_x][new_y] = visit[q[0]][q[1]] + 1

    sum_visit = sum([M - i.count(0) for i in visit])
    return sum_visit


T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [tuple(map(int, input().split())) for _ in range(N)]

    result = bfs(R, C)
    print('#{} {}'.format(test_case, result))
