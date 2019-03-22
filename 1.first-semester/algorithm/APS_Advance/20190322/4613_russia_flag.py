import sys

sys.stdin = open('4613.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []
    for r in range(N):
        temp = list(input())
        matrix.append(temp)

    min_cnt = M * N
    for k in range(1, N):
        must_blue_line = k
        cnt = 0
        for j in range(M):
            if matrix[0][j] != 'W':
                cnt += 1

        for j in range(M):
            if matrix[must_blue_line][j] != 'B':
                cnt += 1

        for j in range(M):
            if matrix[N-1][j] != 'R':
                cnt += 1

        min_temp = 2 * M * N
        flag = False
        for i in range(1, must_blue_line+1):
            cnt_temp = 0
            for ii in range(1, i):
                white_cnt = matrix[ii].count('W')
                cnt_temp += M - white_cnt

            for ii in range(i, must_blue_line):
                blue_cnt = matrix[ii].count('B')
                cnt_temp += M - blue_cnt

            if cnt_temp < min_temp:
                flag = True
                min_temp = cnt_temp

        if flag:
            cnt += min_temp

        min_temp2 = 2 * M * N
        flag = False
        for i in range(must_blue_line+1, N):
            cnt_temp = 0
            for ii in range(must_blue_line+1, i):
                blue_cnt = matrix[ii].count('B')
                cnt_temp += M - blue_cnt

            for ii in range(i, N-1):
                red_cnt = matrix[ii].count('R')
                cnt_temp += M - red_cnt

            if cnt_temp < min_temp2:
                flag = True
                min_temp2 = cnt_temp

        if flag:
            cnt += min_temp2

        if cnt < min_cnt:
            min_cnt = cnt

    print('#{} {}'.format(test_case, min_cnt))
