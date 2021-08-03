import sys
from collections import deque

sys.stdin = open('1240.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input())))

    code = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    for i in range(len(matrix)):
        if sum(matrix[i]) != 0:
            check1 = i
            for j in range(len(matrix[check1])-1, -1, -1):
                if matrix[check1][j] == 1:
                    check2 = j
                    break

            break

    results = deque()
    for _ in range(8):
        temp = deque()
        cnt = 0
        while True:
            if cnt > 6:
                check2 = check2 - cnt
                results.appendleft(temp)
                break

            temp.appendleft(matrix[check1][check2-cnt])
            cnt += 1

    password = deque()
    for result in results:
        password.append(code[''.join(map(str, result))])

    check = ((password[0] + password[2] + password[4] + password[6]) * 3 + password[1] + password[3] + password[5] + password[7]) % 10 == 0

    if check:
        print('#{} {}'.format(test_case, sum(password)))
    else:
        print('#{} {}'.format(test_case, 0))
