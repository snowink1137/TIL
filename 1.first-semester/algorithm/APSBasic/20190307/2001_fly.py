import sys

sys.stdin = open('2001_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    sum_matrix = [[0] * (N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            kill_sum = 0
            for k in range(M):
                kill_sum += matrix[i][j+k]

            sum_matrix[i][j] = kill_sum

    sum_matrix_last = [[0] * (N-M+1) for _ in range(N-M+1)]
    for j in range(N-M+1):
        for i in range(N-M+1):
            kill_sum = 0
            for k in range(M):
                kill_sum += sum_matrix[i+k][j]

            sum_matrix_last[i][j] = kill_sum

    max_list = []
    for row in sum_matrix_last:
        max_list.append(max(row))

    result = max(max_list)

    print('#{} {}'.format(test_case, result))
