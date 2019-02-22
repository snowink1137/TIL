import sys

sys.stdin = open('1210_input.txt')

for test_case in range(1, 11):
    input()
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    i = 99
    j = 0
    for k in range(100):
        if matrix[99][k] & (1 << 1):
            j = k
            break

    direction = 0
    while i > 0:
        if direction == 0:
            i -= 1
            if j == 99:
                if matrix[i][j-1] != 0:
                    direction = -1
            elif j == 0:
                if matrix[i][j+1] != 0:
                    direction = 1
            else:
                if matrix[i][j+1] != 0:
                    direction = 1
                elif matrix[i][j-1] != 0:
                    direction = -1
        elif direction == -1:
            j -= 1
            if j == 0:
                direction = 0
            else:
                if matrix[i-1][j] != 0:
                    direction = 0
        elif direction == 1:
            j += 1
            if j == 99:
                direction = 0
            else:
                if matrix[i-1][j] != 0:
                    direction = 0

    print(f'#{test_case} {j}')


