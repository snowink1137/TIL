dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(M, N, board, visit):
    queue = deque()
    D = [[0] * N for _ in range(M)]

    visit[0][0] = True
    for i in range(4):
        new_x = dx[i]
        new_y = dy[i]

        if 0 <= new_x <= M-1 and 0 <= new_y <= N-1:
            if board[new_x][new_y] == 0:
                queue.append([new_x, new_y])
                D[new_x][new_y] = 1

    while len(queue):
        x, y = queue.popleft()

        if not visit[x][y]:
            visit[x][y] = True

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if 0

    return


def solution(board):
    M = len(board)
    N = len(board[0])

    visit = [[False] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                visit[i][j] = True

    answer = bfs(N, M, board, visit)
    return answer