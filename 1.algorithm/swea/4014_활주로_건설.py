import sys

sys.stdin = open('4014_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    result = 0
    N, X = map(int, input().split())
    geo_matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        used_cell = [False for _ in range(N)]
        for j in range(N-1):
            if abs(geo_matrix[i][j] - geo_matrix[i][j+1]) > 1:
                break
            elif geo_matrix[i][j] == geo_matrix[i][j+1]:
                continue

            flag = False
            if geo_matrix[i][j] > geo_matrix[i][j+1]:
                if j + X > N-1:
                    break

                check = geo_matrix[i][j+1]
                for k in range(j+1, j+1+X):
                    if geo_matrix[i][k] != check or used_cell[k]:
                        break
                else:
                    flag = True
                    for kk in range(j+1, j+1+X):
                        used_cell[kk] = True

                if not flag:
                    break

            else:
                if j - X + 1 < 0:
                    break

                check = geo_matrix[i][j-X+1]
                for k in range(j-X+1, j+1):
                    if geo_matrix[i][k] != check or used_cell[k]:
                        break
                else:
                    flag = True
                    for kk in range(j-X+1, j+1):
                        used_cell[kk] = True

                if not flag:
                    break
        else:
            result += 1

    for j in range(N):
        used_cell = [False for _ in range(N)]
        for i in range(N-1):
            if abs(geo_matrix[i][j] - geo_matrix[i+1][j]) > 1:
                break
            elif geo_matrix[i][j] == geo_matrix[i+1][j]:
                continue

            flag = False
            if geo_matrix[i][j] > geo_matrix[i+1][j]:
                if i + X > N - 1:
                    break

                check = geo_matrix[i+1][j]
                for k in range(i+1, i+1+X):
                    if geo_matrix[k][j] != check or used_cell[k]:
                        break
                else:
                    flag = True
                    for kk in range(i+1, i+1+X):
                        used_cell[kk] = True

                if not flag:
                    break

            else:
                if i - X + 1 < 0:
                    break

                check = geo_matrix[i-X+1][j]
                for k in range(i-X+1, i+1):
                    if geo_matrix[k][j] != check or used_cell[k]:
                        break
                else:
                    flag = True
                    for kk in range(i-X+1, i+1):
                        used_cell[kk] = True

                if not flag:
                    break
        else:
            result += 1

    print('#{} {}'.format(test_case, result))
