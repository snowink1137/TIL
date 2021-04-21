import sys

sys.stdin = open('20057_sample_input.txt', 'r')

N = int(input())
sand_matrix = [list(map(int, input().split())) for _ in range(N)]

result = 0

location = [N//2, N//2]


def tornado(location, direction):
    global result
    acc_sand = 0
    out_sand = 0
    x, y = location[0], location[1]
    sand = sand_matrix[x][y]
    sand_matrix[x][y] = 0

    if direction == 0:
        new_x, new_y = x, y - 2
        temp_sand = int(sand * 0.05)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y - 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y - 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 2, y
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 2, y
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y + 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y + 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y - 1
        temp_sand = sand - acc_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

    elif direction == 1:
        new_x, new_y = x + 2, y
        temp_sand = int(sand * 0.05)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y - 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y + 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y + 1
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y - 1
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y + 2
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y - 2
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y - 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y + 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y
        temp_sand = sand - acc_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

    elif direction == 2:
        new_x, new_y = x, y + 2
        temp_sand = int(sand * 0.05)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y + 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y + 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 2, y
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 2, y
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y - 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y - 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y + 1
        temp_sand = sand - acc_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

    elif direction == 3:
        new_x, new_y = x - 2, y
        temp_sand = int(sand * 0.05)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y + 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y - 1
        temp_sand = int(sand * 0.1)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y - 1
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y + 1
        temp_sand = int(sand * 0.07)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y - 2
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x, y + 2
        temp_sand = int(sand * 0.02)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y - 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x + 1, y + 1
        temp_sand = int(sand * 0.01)
        acc_sand += temp_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

        new_x, new_y = x - 1, y
        temp_sand = sand - acc_sand
        if 0 <= new_x < N and 0 <= new_y < N:
            sand_matrix[new_x][new_y] += temp_sand
        else:
            out_sand += temp_sand

    result += out_sand


for i in range(N//2):
    direction = 0
    location[1] -= 1
    tornado(location, direction)

    direction = 1
    for _ in range(2*i+1):
        location[0] += 1
        tornado(location, direction)

    direction = 2
    for _ in range(2*i+2):
        location[1] += 1
        tornado(location, direction)

    direction = 3
    for _ in range(2*i+2):
        location[0] -= 1
        tornado(location, direction)

    direction = 0
    for _ in range(2*i+2):
        location[1] -= 1
        tornado(location, direction)


print(result)
