import sys

sys.stdin = open('1979_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    found = 0
    for i in range(N):
        for j in range(N - K + 1):
            if j == 0:
                if matrix[i][j + K] == 1:
                    continue

                for k in range(K):
                    if matrix[i][j + k] == 0:
                        break
                else:
                    found += 1

            elif j == N - K:
                if matrix[i][j - 1] == 1:
                    continue

                for k in range(K):
                    if matrix[i][j + k] == 0:
                        break
                else:
                    found += 1

            elif matrix[i][j - 1] == 0 and matrix[i][j + K] == 0:
                for k in range(K):
                    if matrix[i][j + k] == 0:
                        break
                else:
                    found += 1

    for j in range(N):
        for i in range(N - K + 1):
            if i == 0:
                if matrix[i + K][j] == 1:
                    continue

                for k in range(K):
                    if matrix[i + k][j] == 0:
                        break
                else:
                    found += 1

            elif i == N - K:
                if matrix[i - 1][j] == 1:
                    continue

                for k in range(K):
                    if matrix[i + k][j] == 0:
                        break
                else:
                    found += 1

            elif matrix[i - 1][j] == 0 and matrix[i + K][j] == 0:
                for k in range(K):
                    if matrix[i + k][j] == 0:
                        break
                else:
                    found += 1

    print('#{} {}'.format(test_case, found))
