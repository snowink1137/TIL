import sys

sys.stdin = open('4131.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, X = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    cnt = 0
    for i in range(N):
        break_index = [0]
        top = 0
        for j in range(N-1):
            if matrix[i][j] > top:
                top = matrix[i][j]

            if matrix[i][j] != matrix[i][j+1]:
                break_index.append(j+1)

        break_index.append(N)
        if len(break_index) == 2:
            cnt += 1
        else:
            for k in range(len(break_index)-1):
                if break_index[k+1] - break_index[k] < X:
                    if break_index[k+1] > N-1:
                        break
                    if matrix[i][break_index[k+1]] != top:
                        break
            else:
                cnt += 1

    print(cnt)
