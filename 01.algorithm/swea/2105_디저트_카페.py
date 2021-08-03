import sys

sys.stdin = open('2105_sample_input.txt', 'r')

dx = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
dy = [[1, -1], [-1, -1], [-1, 1], [1, 1]]


def dfs(x, y, k, direction):
    global result, start_x, start_y

    if direction > 3:
        return

    if x == start_x and y == start_y:
        if direction == 0:
            pass
        else:
            if k > result:
                result = k

            return

    for i in range(2):
        if x == start_x and y == start_y and direction == 0 and i == 1:
            return

        new_x = x + dx[direction][i]
        new_y = y + dy[direction][i]

        if (not 0 <= new_x <= N-1) or (not 0 <= new_y <= N-1) or visit_map[new_x][new_y]:
            continue

        if visit_dessert[dessert_map[new_x][new_y]] or dessert_map[new_x][new_y] == start_dessert:
            if new_x == start_x and new_y == start_y:
                pass
            else:
                continue

        visit_map[new_x][new_y] = True
        visit_dessert[dessert_map[new_x][new_y]] = True

        if i == 0:
            dfs(new_x, new_y, k+1, direction)
        else:
            dfs(new_x, new_y, k+1, direction+1)

        visit_map[new_x][new_y] = False
        visit_dessert[dessert_map[new_x][new_y]] = False

    return


T = int(input())
for test_case in range(1, T+1):
    result = -1
    N = int(input())

    dessert_map = [list(map(int, input().split())) for _ in range(N)]
    visit_map = [[False for _ in range(N)] for _ in range(N)]
    visit_dessert = [False for _ in range(101)]
    for i in range(N-2):
        for j in range(1, N-1):
            start_x = i
            start_y = j
            start_dessert = dessert_map[i][j]
            dfs(i, j, 0, 0)

    print('#{} {}'.format(test_case, result))

