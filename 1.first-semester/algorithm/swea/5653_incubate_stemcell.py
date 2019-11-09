import sys

sys.stdin = open('5653.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    result = 0
    queue = []

    matrix = [[0 for _ in range(350)] for _ in range(350)]

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            temp = row.pop(0)

            if temp != 0:
                matrix[i+150][j+150] = [temp, temp-1]
                if temp == 1:
                    queue.append((i+150, j+150))

    for _ in range(K-1):
        while len(queue):
            q = queue.pop()

            for i in range(4):
                new_x = q[0] + dx[i]
                new_y = q[1] + dy[i]

                if matrix[new_x][new_y] != 0:
                    if matrix[new_x][new_y][0] == matrix[new_x][new_y][1] and matrix[q[0]][q[1]][0] > matrix[new_x][new_y][0]:
                        matrix[new_x][new_y] = [matrix[q[0]][q[1]][0], matrix[q[0]][q[1]][0]]
                else:
                    matrix[new_x][new_y] = [matrix[q[0]][q[1]][0], matrix[q[0]][q[1]][0]]

        for i in range(350):
            for j in range(350):
                if matrix[i][j] == 0:
                    continue

                if matrix[i][j][1] > 0:
                    matrix[i][j][1] -= 1
                elif matrix[i][j][1] == 0:
                    matrix[i][j][1] -= 1
                    queue.append((i, j))
                elif matrix[i][j][0] == abs(matrix[i][j][1]):
                    pass
                else:
                    matrix[i][j][1] -= 1
                    queue.append((i, j))

    for i in range(350):
        for j in range(350):
            if matrix[i][j] != 0 and matrix[i][j][0] > abs(matrix[i][j][1]):
                result += 1

    print('#{} {}'.format(test_case, result))
