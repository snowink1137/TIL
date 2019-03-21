import sys

sys.stdin = open('1216_input.txt')

N = 100
for test_case in range(1, 11):
    input()
    matrix = []
    for i in range(N):
        matrix.append(input())

    flag = False
    max_length = 0
    for M in range(N, 0, -1):
        for t in range(N-M+1):
            for i in range(N):
                for j in range(M):
                    if matrix[i][t+j] != matrix[i][t+M-j-1]:
                        break
                else:
                    if M > max_length:
                        max_length = M
                        flag = True
                        break
            if flag:
                break

            for j in range(N):
                for i in range(M):
                    if matrix[t+i][j] != matrix[t+M-i-1][j]:
                        break
                else:
                    if M > max_length:
                        max_length = M
                        flag = True
                        break
            if flag:
                break
        if flag:
            break

    print(f'#{test_case} {max_length}')
