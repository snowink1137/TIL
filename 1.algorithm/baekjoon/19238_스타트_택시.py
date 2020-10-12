import sys
from collections import deque

sys.stdin = open('19238_sample_input.txt', 'r')
N, M, F = map(int, input().split())

navi_map = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(int, input().split()))
customers = [list(map(int, input().split())) for _ in range(M)]
customers_start = {}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def calculate_distance(start, end):
    queue = deque()
    queue.append(start)
    visit = [[0 for _ in range(N)] for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not (0 <= new_x < N and 0 <= new_y < N and not navi_map[new_x][new_y]):
                continue

            if visit[new_x][new_y]:
                continue

            visit[new_x][new_y] = visit[x][y] + 1
            queue.append((new_x, new_y))

            if new_x == end[0] and new_y == end[1]:
                return visit[new_x][new_y]


def find(taxi):
    queue = deque()
    queue.append(taxi)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    nearest_customer = M
    flag = False

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not (0 <= new_x < N and 0 <= new_y < N and navi_map[new_x][new_y] != 1):
                continue

            if visit[new_x][new_y]:
                continue

            visit[new_x][new_y] = visit[x][y] + 1
            if not flag:
                queue.append((new_x, new_y))

            if type(customers_start.get((new_x, new_y))) == int:
                if customers_start[(new_x, new_y)] < nearest_customer:
                    nearest_customer = customers_start[(new_x, new_y)]
                    flag = True

    return nearest_customer


# 손님 최단 거리 계산
for i in range(len(customers)):
    customers[i].append(calculate_distance([customers[i][0], customers[i][1]], [customers[i][2], customers[i][3]]))
    customers_start[(customers[i][0], customers[i][1])] = i

# 택시 운행
while True:
    if F <= 0:
        if len(customers):
            result = -1
        else:
            result = 0

    next_customer = find(taxi)






print(result)
