import sys

sys.stdin = open('21610_sample_input.txt', 'r')

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]


def move(clouds, d, s):
    global N

    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        new_x = (x + dx[d-1] * s) % N
        new_y = (y + dy[d-1] * s) % N
        cloud[0], cloud[1] = new_x, new_y

    return


def rain(clouds, matrix):
    for cloud in clouds:
        matrix[cloud[0]][cloud[1]] += 1


def water_copy(clouds, matrix):
    global N

    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        for i in range(4):
            new_x = x + dx[2*i+1]
            new_y = y + dy[2*i+1]

            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            if matrix[new_x][new_y] < 1:
                continue

            matrix[x][y] += 1


def make_clouds(clouds, matrix):
    global N

    clouds_check = [[False for _ in range(N)] for _ in range(N)]
    for cloud in clouds:
        clouds_check[cloud[0]][cloud[1]] = True

    new_clouds = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] < 2:
                continue

            if clouds_check[i][j]:
                continue

            new_clouds.append([i, j])
            matrix[i][j] -= 2

    return new_clouds


for command in commands:
    d, s = command[0], command[1]
    move(clouds, d, s)

    rain(clouds, matrix)

    water_copy(clouds, matrix)

    clouds = make_clouds(clouds, matrix)

answer = sum(map(sum, matrix))
print(answer)
