import sys

sys.stdin = open('21611_sample_input.txt', 'r')

from collections import deque

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

queue = deque()
x, y = N // 2, N // 2
interface = []

direction, change, cnt = 3, 0, 0
while True:
    if cnt >= change:
        if direction == 3 or direction == 1:
            change += 1

        cnt = 0
        direction = (direction + 1) % 4

    new_x, new_y = x + dx[direction], y + dy[direction]
    interface.append([new_x, new_y])
    cnt += 1
    x, y = new_x, new_y

    if new_x == 0 and new_y == 0:
        break

interface_to_coordinate = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(interface)):
    if matrix[interface[i][0]][interface[i][1]] != 0:
        queue.append(matrix[interface[i][0]][interface[i][1]])

    interface_to_coordinate[interface[i][0]][interface[i][1]] = i

answer = 0


def magic(matrix, d, s):
    global N
    target = []
    x, y = N // 2, N // 2

    if d == 1:
        dd = 3
    elif d == 2:
        dd = 1
    elif d == 3:
        dd = 0
    else:
        dd = 2

    for ss in range(1, s+1):
        target.append([x+dx[dd]*ss, y+dy[dd]*ss])

    return target


def score(matrix, destroyed_area):
    result = 0
    for area in destroyed_area:
        if matrix[area[0]][area[1]] == 1:
            result += 1
        elif matrix[area[0]][area[1]] == 2:
            result += 2
        elif matrix[area[0]][area[1]] == 3:
            result += 3

    return result


def move(queue, destroyed_area):
    global N

    temp = []

    for area in destroyed_area:
        x, y = area[0], area[1]
        idx = interface_to_coordinate[x][y]

        temp.append(idx)

    temp.sort(reverse=True)
    for idx in temp:
        del queue[idx]

    new_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(queue)):
        x, y = interface[i][0], interface[i][1]
        new_matrix[x][y] = queue[i]

    return new_matrix


def explode(queue):
    target = []

    cnt = 1
    for i in range(1, len(queue)):
        if queue[i] != queue[i-1]:
            if cnt > 3:
                for j in range(i-cnt, i):
                    target.append(interface[j])

            cnt = 1
        else:
            cnt += 1

    if cnt > 3:
        for j in range(len(queue) - cnt, len(queue)):
            target.append(interface_to_coordinate[j])

    return target


def increase(queue):
    global N

    new_queue = deque()

    cnt = 0
    buffer = 0
    while queue:
        q = queue.popleft()

        if buffer == 0:
            buffer = q
            cnt = 1
            continue

        if buffer == q:
            cnt += 1
            continue

        if buffer != q:
            if len(new_queue) > N * N - 2:
                break
            new_queue.append(cnt)

            if len(new_queue) > N * N - 2:
                break

            new_queue.append(buffer)
            buffer = q
            cnt = 1

    if buffer != 0:
        if len(new_queue) > N*N-2:
            return new_queue

        new_queue.append(cnt)

        if len(new_queue) > N*N-2:
            return new_queue

        new_queue.append(buffer)

    return new_queue


for command in commands:
    d, s = command[0], command[1]
    destroyed_area = magic(matrix, d, s)

    # answer += score(matrix, destroyed_area)

    while destroyed_area:
        matrix = move(queue, destroyed_area)
        destroyed_area = explode(queue)
        answer += score(matrix, destroyed_area)

    queue = increase(queue)
    matrix = move(queue, destroyed_area)

print(answer)


