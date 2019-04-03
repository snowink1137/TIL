import sys

sys.stdin = open('1868.txt', 'r')

dx = (0, 1, 1, 1, 0, -1, -1, -1)
dy = (1, 1, 0, -1, -1, -1, 0, 1)


def check(x, y):
    cnt = 0
    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < N and matrix[new_x][new_y] == '*':
            cnt += 1

    return cnt


def check_zero(x, y):
    global mark

    if matrix[x][y] == mark:
        return

    matrix[x][y] = mark

    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < N:
            element = matrix[new_x][new_y]

            if element == 0:
                check_zero(new_x, new_y)
            elif element == '*':
                continue
            elif element == mark:
                continue
            else:
                matrix[new_x][new_y] = mark


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            target = matrix[i][j]
            if target == '*':
                continue
            elif target == '.':
                matrix[i][j] = check(i, j)

    mark = -1
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                check_zero(i, j)
                mark -= 1

    result = 0
    for i in range(N):
        for j in range(N):
            target = matrix[i][j]
            if target == '*':
                continue
            elif target > 0:
                result += 1

    result -= mark + 1
    print('#{} {}'.format(test_case, result))
