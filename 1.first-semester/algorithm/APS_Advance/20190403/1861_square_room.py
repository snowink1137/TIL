import sys
from collections import deque

sys.stdin = open('1861.txt', 'r')

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def bfs(x, y):
    global result
    global result_value

    cnt = 1
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True

    temp = []
    temp.append((matrix[x][y], x, y))
    while len(queue):
        q = queue.popleft()
        for i in range(4):
            new_x = q[0] + dx[i]
            new_y = q[1] + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N and not visit[new_x][new_y] and abs(matrix[new_x][new_y] - matrix[q[0]][q[1]]) == 1:
                queue.append((new_x, new_y))
                visit[new_x][new_y] = True
                temp.append((matrix[new_x][new_y], new_x, new_y))
                cnt += 1

    if cnt > result:
        result = cnt
        temp.sort(key=lambda x: x[0])
        result_value = temp[0][0]
    elif cnt == result:
        temp.sort(key=lambda x: x[0])
        if temp[0][0] < result_value:
            result_value = temp[0][0]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 1
    result_value = 0xffffffffff
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print('#{} {} {}'.format(test_case, result_value, result))
