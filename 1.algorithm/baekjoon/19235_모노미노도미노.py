import sys

sys.stdin = open('19235_sample_input.txt', 'r')

N = int(input().split())
result = 0
green_board = [[0 for _ in range(4)] for _ in range(6)]
blue_board = [[0 for _ in range(4)] for _ in range(6)]


def drop_block(y, board):
    x = 0
    while True:
        if x == 6:
            return 5

        if board[x][y]:
            return x-1

        x += 1

    return x


def down(board):
    visit = {}
    for x in range()


def check_result(board):
    global result
    flag = False
    for x in range(5, 1, -1):
        cnt = 0
        for y in range(4):
            if board[x][y]:
                cnt += 1

        if cnt == 4:
            result += 1
            for y in range(4):
                board[x][y] = 0

            flag = True

    if flag:
        down(board)
        check_result(board)


def check_boundary(board):
    pass


for block_number in range(1, N+1):
    t, x, y = map(int, input().split())

    if t == 1:
        new_green_idx = drop_block(y, green_board)
        green_board[new_green_idx][y] = block_number

        new_blue_idx = drop_block(x, blue_board)
        blue_board[new_blue_idx][x] = block_number
    elif t == 2:
        new_green_idx1 = drop_block(y, green_board)
        new_green_idx2 = drop_block(y+1, green_board)
        new_green_idx = min(new_green_idx1, new_green_idx2)
        green_board[new_green_idx][y] = block_number
        green_board[new_green_idx][y+1] = block_number

        new_blue_idx = drop_block(x, blue_board)
        blue_board[new_blue_idx][x] = block_number
        new_blue_idx = drop_block(x, blue_board)
        blue_board[new_blue_idx][x] = block_number
    elif t == 3:
        new_green_idx = drop_block(y, green_board)
        green_board[new_green_idx][y] = block_number
        new_green_idx = drop_block(y, green_board)
        green_board[new_green_idx][y] = block_number

        new_blue_idx1 = drop_block(x, blue_board)
        new_blue_idx2 = drop_block(x+1, blue_board)
        new_blue_idx = min(new_blue_idx1, new_blue_idx2)
        blue_board[new_blue_idx][x] = block_number
        blue_board[new_blue_idx][x+1] = block_number

    check_result(green_board)
    check_result(blue_board)
    check_boundary(green_board)
    check_boundary(blue_board)

cnt = 0
for i in range(6):
    for j in range(4):
        if green_board[i][j]:
            cnt += 1

        if blue_board[i][j]:
            cnt += 1

print(result)
print(cnt)
