import sys

sys.stdin = open('2819.txt', 'r')

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def go(x, y, k=1, string=''):
    if k == 8:
        result_set.add(string)
        return

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < 4 and 0 <= new_y < 4:
            go(new_x, new_y, k+1, string+matrix[x][y])


T = int(input())
for test_case in range(1, T+1):
    matrix = [input().split() for _ in range(4)]

    result_set = set()
    for i in range(4):
        for j in range(4):
            go(i, j)

    print('#{} {}'.format(test_case, len(result_set)))
