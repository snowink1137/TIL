import sys

sys.stdin = open('1220_input.txt', 'r')

for test_case in range(1, 11):
    input()

    matrix = []
    for i in range(100):
        matrix.append(input().split())

    cnt = 0
    for j in range(100):
        direction = 0
        for i in range(100):
            if matrix[i][j] == '0':
                continue
            elif direction == 0:
                if matrix[i][j] == '2':
                    continue
                else:
                    direction = 1
            elif direction == 1:
                if matrix[i][j] == '2':
                    cnt += 1
                    direction = 2
            elif direction == 2:
                if matrix[i][j] == '1':
                    direction = 1

    print(f'#{test_case} {cnt}')
