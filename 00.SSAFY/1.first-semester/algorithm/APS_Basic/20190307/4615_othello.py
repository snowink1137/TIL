import sys

sys.stdin = open('4615_sample_input.txt', 'r')


def check(index, color):
    right_result = False
    for j in range(index[1] + 1, N):
        if matrix[index[0]][j] == 0:
            break

        if matrix[index[0]][j] == color:
            right_result = [index[0], j]
            break

    left_result = False
    for j in range(index[1] - 1, -1, -1):
        if matrix[index[0]][j] == 0:
            break

        if matrix[index[0]][j] == color:
            left_result = [index[0], j]
            break

    south_result = False
    for i in range(index[0] + 1, N):
        if matrix[i][index[1]] == 0:
            break

        if matrix[i][index[1]] == color:
            south_result = [i, index[1]]
            break

    north_result = False
    for i in range(index[0] - 1, -1, -1):
        if matrix[i][index[1]] == 0:
            break

        if matrix[i][index[1]] == color:
            north_result = [i, index[1]]
            break

    ten_direction = False
    low = index[0] if index[0] < index[1] else index[1]
    for i in range(1, low + 1):
        if matrix[index[0] - i][index[1] - i] == 0:
            break

        if matrix[index[0] - i][index[1] - i] == color:
            ten_direction = [index[0] - i, index[1] - i]
            break

    four_direction = False
    high = index[0] if index[0] > index[1] else index[1]
    for i in range(1, N-high):
        if matrix[index[0] + i][index[1] + i] == 0:
            break

        if matrix[index[0] + i][index[1] + i] == color:
            four_direction = [index[0] + i, index[1] + i]
            break

    temp_i = index[0]
    temp_j = index[1]
    flag = False
    while True:
        if temp_i + 1 >= N or temp_j - 1 < 0:
            if flag:
                seven_direction = [temp_i, temp_j]
                break
            else:
                seven_direction = False
                break
        else:
            if flag:
                seven_direction = [temp_i, temp_j]
                break

            temp_i += 1
            temp_j -= 1

            if matrix[temp_i][temp_j] == 0:
                seven_direction = False
                break

            if matrix[temp_i][temp_j] == color:
                flag = True

    temp_i = index[0]
    temp_j = index[1]
    flag = False
    while True:
        if temp_i - 1 < 0 or temp_j + 1 >= N:
            if flag:
                one_direction = [temp_i, temp_j]
                break
            else:
                one_direction = False
                break
        else:
            if flag:
                one_direction = [temp_i, temp_j]
                break

            temp_i -= 1
            temp_j += 1

            if matrix[temp_i][temp_j] == 0:
                one_direction = False
                break

            if matrix[temp_i][temp_j] == color:
                flag = True

    return [right_result, left_result, south_result, north_result, ten_direction, four_direction, seven_direction, one_direction]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [[0] * N for _ in range(N)]

    first = (N // 2) - 1
    matrix[first][first] = 2
    matrix[first + 1][first + 1] = 2
    matrix[first][first + 1] = 1
    matrix[first + 1][first] = 1

    information = []
    for m in range(M):
        information.append(list(map(int, input().split())))

    for info in information:
        color = info[2]
        j = info[0] - 1
        i = info[1] - 1
        current_index = [i, j]

        matrix[current_index[0]][current_index[1]] = color
        index_list = check(current_index, color)

        for k in range(8):
            if not index_list[k]:
                continue

            if k == 0:
                for j in range(current_index[1] + 1, index_list[k][1]):
                    matrix[current_index[0]][j] = color
            elif k == 1:
                for j in range(current_index[1] - 1, index_list[k][1], -1):
                    matrix[current_index[0]][j] = color
            elif k == 2:
                for i in range(current_index[0] + 1, index_list[k][0]):
                    matrix[i][current_index[1]] = color
            elif k == 3:
                for i in range(current_index[0] - 1, index_list[k][0], -1):
                    matrix[i][current_index[1]] = color
            elif k == 4:
                for j in range(1, current_index[0] - index_list[k][0]):
                    matrix[current_index[0] - j][current_index[1] - j] = color
            elif k == 5:
                for j in range(1, index_list[k][0] - current_index[0]):
                    matrix[current_index[0] + j][current_index[1] + j] = color
            elif k == 6:
                for j in range(1, index_list[k][0] - current_index[0]):
                    matrix[current_index[0] + j][current_index[1] - j] = color
            elif k == 7:
                for j in range(1, current_index[0] - index_list[k][0]):
                    matrix[current_index[0] - j][current_index[1] + j] = color

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                black += 1
            elif matrix[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(test_case, black, white))
