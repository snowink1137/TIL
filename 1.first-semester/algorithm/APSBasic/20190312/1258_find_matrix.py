import sys

sys.stdin = open('1258.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    visit = [[False] * N for _ in range(N)]

    cnt = 0
    result = []
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
               continue
            else:
                if matrix[i][j] != 0:
                    x = i + 1
                    start_x = i
                    while x <= N-1 and matrix[x][j] != 0:
                        x += 1

                    y = j + 1
                    start_y = j
                    while y <= N-1 and matrix[i][y] != 0:
                        y += 1

                    cnt += 1

                    height = x - start_x
                    width = y - start_y
                    size = height * width

                    for ii in range(start_x, x):
                        for jj in range(start_y, y):
                            visit[ii][jj] = True

                    result.append([size, height, width])

    result.sort(key=lambda x: (x[0], x[1]))
    result_list = []
    for elem in result:
        result_list.append(elem[1])
        result_list.append(elem[2])

    print('#{} {} {}'.format(test_case, cnt, ' '.join(map(str, result_list))))
