import sys

sys.stdin = open('5650_sample_input.txt', 'r')

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def start(i, j, d):
    point = 0
    new_i = i
    new_j = j
    new_d = d

    while True:
        new_i += dx[new_d]
        new_j += dy[new_d]

        if (new_i == i and new_j == j) or (matrix[new_i][new_j] == -1):
            return point

        if matrix[new_i][new_j] == 0:
            continue

        if 6 <= matrix[new_i][new_j] <= 10:
            new_i, new_j = worm_hole[(new_i, new_j)]
            continue

        point += 1
        if matrix[new_i][new_j] == 1:
            if new_d == 0 or new_d == 3:
                new_d = (new_d + 2) % 4
            elif new_d == 1:
                new_d = 0
            else:
                new_d = 3
        elif matrix[new_i][new_j] == 2:
            if new_d == 0 or new_d == 1:
                new_d = (new_d + 2) % 4
            elif new_d == 2:
                new_d = 1
            else:
                new_d = 0
        elif matrix[new_i][new_j] == 3:
            if new_d == 1 or new_d == 2:
                new_d = (new_d + 2) % 4
            elif new_d == 0:
                new_d = 1
            else:
                new_d = 2
        elif matrix[new_i][new_j] == 4:
            if new_d == 2 or new_d == 3:
                new_d = (new_d + 2) % 4
            elif new_d == 0:
                new_d = 3
            else:
                new_d = 2
        elif matrix[new_i][new_j] == 5:
            new_d = (new_d + 2) % 4

    return point


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = 0
    matrix = [[5] + list(map(int, input().split())) + [5] for _ in range(N)]
    matrix.insert(0, [5] * (N+2))
    matrix.append([5] * (N+2))

    temp_worm_hole = {}
    for i in range(1, N+1):
        for j in range(1, N+1):
            if 6 <= matrix[i][j] <= 10:
                if temp_worm_hole.get(matrix[i][j]):
                    temp_worm_hole[matrix[i][j]].append((i, j))
                else:
                    temp_worm_hole[matrix[i][j]] = [(i, j)]

    worm_hole = {}
    for worm_hole_list in temp_worm_hole.values():
        worm_hole[worm_hole_list[0]] = worm_hole_list[1]
        worm_hole[worm_hole_list[1]] = worm_hole_list[0]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j]:
                continue

            for d in range(4):
                temp = start(i, j, d)
                if temp > result:
                    result = temp

    print('#{} {}'.format(test_case, result))


