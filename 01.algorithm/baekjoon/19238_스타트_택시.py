import sys
from collections import deque

sys.stdin = open('19238_sample_input.txt', 'r')
N, M, F = map(int, input().split())

navi_map = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(lambda x: int(x)-1, input().split()))
customers = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
customers_start = {}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def calculate_distance(start, end):
    queue = deque()
    queue.append(start)
    visit = [[False for _ in range(N)] for _ in range(N)]
    step = [[0 for _ in range(N)] for _ in range(N)]
    visit[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not (0 <= new_x < N and 0 <= new_y < N and not navi_map[new_x][new_y]):
                continue

            if visit[new_x][new_y]:
                continue

            visit[new_x][new_y] = True
            step[new_x][new_y] += step[x][y] + 1

            if new_x == end[0] and new_y == end[1]:
                return step[new_x][new_y]
            else:
                queue.append((new_x, new_y))


def find(taxi):
    if customers_start.get((taxi[0], taxi[1])):
        return tuple(taxi), 0

    queue = deque()
    queue.append(taxi)
    visit = [[False for _ in range(N)] for _ in range(N)]
    step = [[0 for _ in range(N)] for _ in range(N)]
    visit[taxi[0]][taxi[1]] = True
    nearest_customer_list = []
    distance = N * N

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not (0 <= new_x < N and 0 <= new_y < N and navi_map[new_x][new_y] != 1):
                continue

            if visit[new_x][new_y]:
                continue

            visit[new_x][new_y] = True

            step_distance = step[x][y] + 1
            if step_distance > distance:
                continue

            step[new_x][new_y] = step_distance

            if customers_start.get((new_x, new_y)):
                temp_customer = (new_x, new_y)

                if step_distance == distance:
                    nearest_customer_list.append(temp_customer)
                else:
                    distance = step_distance
                    nearest_customer_list = [temp_customer]
            else:
                queue.append((new_x, new_y))

    if nearest_customer_list:
        nearest_customer_list.sort()
        return nearest_customer_list[0], distance

    return None, None

# 손님 최단 거리 계산
impossible = False
for i in range(len(customers)):
    distance = calculate_distance([customers[i][0], customers[i][1]], [customers[i][2], customers[i][3]])
    if not distance:
        impossible = True

    customers_start[(customers[i][0], customers[i][1])] = (customers[i][2], customers[i][3], distance)

# 택시 운행
while True:
    if impossible:
        result = -1
        break

    if not len(customers_start):
        result = F
        break

    next_customer, next_customer_distance = find(taxi)
    if next_customer is None:
        if len(customers_start):
            result = -1
            break
        else:
            result = F
            break

    if next_customer_distance + customers_start[next_customer][2] > F:
        result = -1
        break

    F = F - next_customer_distance + customers_start[next_customer][2]
    taxi = customers_start[next_customer][:2]
    customers_start.pop(next_customer)

print(result)
