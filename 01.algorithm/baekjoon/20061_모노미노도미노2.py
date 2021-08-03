import sys

sys.stdin = open('20061_sample_input.txt', 'r')

score, number = 0, 0

N = int(input())

blocks = [list(map(int, input().split())) for _ in range(N)]

green_matrix = [[False for _ in range(4)] for _ in range(6)]
blue_matrix = [[False for _ in range(4)] for _ in range(6)]


def stack(color, location, type_num):
    new_x, new_y = location

    if color == 'green':
        if type_num == 0:
            for i in range(2, 6):
                if green_matrix[i][new_y]:
                    green_matrix[i-1][new_y] = True
                    break
            else:
                green_matrix[5][new_y] = True
        elif type_num == 1:
            for i in range(2, 6):
                if green_matrix[i][new_y] or green_matrix[i][new_y+1]:
                    green_matrix[i-1][new_y] = True
                    green_matrix[i-1][new_y+1] = True
                    break
            else:
                green_matrix[5][new_y] = True
                green_matrix[5][new_y+1] = True
        elif type_num == 2:
            for i in range(2, 6):
                if green_matrix[i][new_y]:
                    green_matrix[i-1][new_y] = True
                    green_matrix[i-2][new_y] = True
                    break
            else:
                green_matrix[5][new_y] = True
                green_matrix[4][new_y] = True
    elif color == 'blue':
        if type_num == 0:
            for i in range(2, 6):
                if blue_matrix[i][new_x]:
                    blue_matrix[i-1][new_x] = True
                    break
            else:
                blue_matrix[5][new_x] = True
        elif type_num == 1:
            for i in range(2, 6):
                if blue_matrix[i][new_x]:
                    blue_matrix[i-1][new_x] = True
                    blue_matrix[i-2][new_x] = True
                    break
            else:
                blue_matrix[5][new_x] = True
                blue_matrix[4][new_x] = True
        elif type_num == 2:
            for i in range(2, 6):
                if blue_matrix[i][new_x] or blue_matrix[i][new_x+1]:
                    blue_matrix[i-1][new_x] = True
                    blue_matrix[i-1][new_x+1] = True
                    break
            else:
                blue_matrix[5][new_x] = True
                blue_matrix[5][new_x+1] = True


def clear(matrix):
    global score

    for i in range(5, -1, -1):
        if sum(matrix[i]) != 4:
            continue

        score += 1

        for ii in range(i, 0, -1):
            for j in range(4):
                matrix[ii][j] = matrix[ii-1][j]
        else:
            for j in range(4):
                matrix[0][j] = False

        if sum(matrix[i]) == 4:
            score += 1

            for ii in range(i, 1, -1):
                for j in range(4):
                    matrix[ii][j] = matrix[ii-1][j]

    return


def push(matrix):
    step = 0
    if sum(matrix[1]):
        step += 1

    if sum(matrix[0]):
        step += 1

    if not step:
        return

    for i in range(5, -1+step, -1):
        for j in range(4):
            matrix[i][j] = matrix[i-step][j]
    else:
        for i in range(2):
            for j in range(4):
                matrix[i][j] = False

    return


for block in blocks:
    t, x, y = block

    stack('green', [x, y], t-1)
    stack('blue', [x, y], t-1)

    clear(green_matrix)
    clear(blue_matrix)

    push(green_matrix)
    push(blue_matrix)


for i in range(len(green_matrix)):
    number += sum(green_matrix[i])

for i in range(len(blue_matrix)):
    number += sum(blue_matrix[i])

print(score)
print(number)
