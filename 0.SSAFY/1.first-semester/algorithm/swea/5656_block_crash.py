import sys

sys.stdin = open('5656.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(column, depth, output):
    global result

    if depth == N+1:
        number = 0
        for i in range(H):
            for j in range(W):
                if output[i][j] != 0:
                    number += 1

        if number < result:
            result = number

        return

    temp1 = [tmp[:] for tmp in output]
    queue = []

    for i in range(H):
        if temp1[i][column] != 0:
            queue.append((i, column, temp1[i][column]))
            break

    while len(queue):
        q = queue.pop(0)
        temp1[q[0]][q[1]] = 0

        for k in range(q[2]):
            for i in range(4):
                new_x = q[0] + k * dx[i]
                new_y = q[1] + k * dy[i]

                if 0 <= new_x < H and 0 <= new_y < W and temp1[new_x][new_y] != 0:
                    queue.append((new_x, new_y, temp1[new_x][new_y]))

    # temp2에 싹 정리해서 보내기
    temp2 = [[0 for _ in range(W)] for _ in range(H)]
    for j in range(W):
        temp3 = []
        for i in range(H):
            if temp1[i][j] != 0:
                temp3.append(temp1[i][j])

        for i in range(H-1, H-1-len(temp3), -1):
            temp2[i][j] = temp3.pop(-1)

    for j in range(W):
        dfs(j, depth+1, temp2)


T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    result = 0xfffffff

    for j in range(W):
        dfs(j, 1, matrix)

    print('#{} {}'.format(test_case, result))
