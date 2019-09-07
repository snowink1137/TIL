dx_direction1 = [0, 1, 1]
dy_direction1 = [1, 0, 0]
dx_direction2 = [0, 1, 0]
dy_direction2 = [1, 0, 1]
M = 0
N = 0
answer = 0


def dfs(board, x, y, direction, time):
    global answer

    if answer != 0:
        return

    if x == M-1 and y == N-1:
        answer = time
        return

    if direction == 1:
        for i in range(3):
            new_x = x + dx_direction1[i]
            new_y = y + dy_direction1[i]

            if 0 <= new_x < M and 0 <= new_y < N:
                if i == 0:
                    if board[new_x][new_y] == 0:
                        dfs(board, new_x, new_y, 1, time+1)
                elif i == 1:
                    if board[new_x][new_y] == 0:
                        if 0 <= new_x < M and 0 <= new_y - 1 < N and board[new_x][new_y-1] == 0:
                            dfs(board, new_x, new_y, 1, time+1)
                else:
                    if board[new_x][new_y] == 0:
                        if 0 <= new_x < M and 0 <= new_y - 1 < N and board[new_x][new_y-1] == 0:
                            dfs(board, new_x, new_y, 2, time+1)
    else:
        for i in range(3):
            new_x = x + dx_direction2[i]
            new_y = y + dy_direction2[i]

            if 0 <= new_x < M and 0 <= new_y < N:
                if i == 0:
                    if board[new_x][new_y] == 0:
                        dfs(board, new_x, new_y, 2, time+1)
                elif i == 1:
                    if board[new_x][new_y] == 0:
                        if 0 <= new_x - 1 < M and 0 <= new_y < N and board[new_x-1][new_y] == 0:
                            dfs(board, new_x, new_y, 2, time+1)
                else:
                    if board[new_x][new_y] == 0:
                        if 0 <= new_x - 1 < M and 0 <= new_y < N and board[new_x-1][new_y] == 0:
                            dfs(board, new_x, new_y, 1, time+1)

    return


def solution(board):
    global answer, M, N

    M = len(board)
    N = len(board[0])
    dfs(board, 0, 1, 1, 0)
    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
