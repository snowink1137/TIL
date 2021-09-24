# bfs 중간에 끊어주니까 시간초과 안남

from collections import defaultdict, deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 2 ** 16


def solution(board, r, c):
    global answer

    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[board[i][j]].append([i, j])

    find(0, board, cards, r, c)

    return answer


def distance(board, x1, y1, x2, y2):
    queue = deque()
    queue.append([x1, y1])
    visit = [[0 for _ in range(4)] for _ in range(4)]

    while queue:
        q = queue.popleft()
        x, y = q[0], q[1],

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if not (0 <= new_x < 4 and 0 <= new_y < 4) or (new_x == x1 and new_y == y1):
                continue

            if visit[new_x][new_y] != 0 and (visit[new_x][new_y] <= visit[x][y] + 1):
                continue

            visit[new_x][new_y] = visit[x][y] + 1
            queue.append([new_x, new_y])
            if new_x == x2 and new_y == y2:
                return visit[x2][y2]

        for i in range(4):
            for t in range(1, 4):
                new_x, new_y = x + dx[i] * t, y + dy[i] * t
                if not (0 <= new_x < 4 and 0 <= new_y < 4) or (new_x == x1 and new_y == y1):
                    continue

                if board[new_x][new_y] != 0:
                    break
            else:
                if i == 0:
                    new_x, new_y = x, 3
                elif i == 1:
                    new_x, new_y = 3, y
                elif i == 2:
                    new_x, new_y = x, 0
                elif i == 3:
                    new_x, new_y = 0, y

            if visit[new_x][new_y] != 0 and (visit[new_x][new_y] <= visit[x][y] + 1):
                continue

            if new_x == x1 and new_y == y1:
                continue

            visit[new_x][new_y] = visit[x][y] + 1
            queue.append([new_x, new_y])
            if new_x == x2 and new_y == y2:
                return visit[x2][y2]

    return visit[x2][y2]


def find(score, board, cards, x0, y0):
    global answer

    if not cards:
        if score < answer:
            answer = score
        return

    next_cards = {}
    for k, v in cards.items():
        next_cards[k] = [v[0][:], v[1][:]]

    for key, value in cards.items():
        x1, y1 = value[0]
        x2, y2 = value[1]
        d1 = distance(board, x0, y0, x1, y1)
        d2 = distance(board, x0, y0, x2, y2)
        d3 = distance(board, x1, y1, x2, y2)
        d4 = distance(board, x2, y2, x1, y1)

        next_cards.pop(key)
        board[x1][y1], board[x2][y2] = 0, 0
        find(score+d1+d3+2, board, next_cards, x2, y2)
        find(score+d2+d4+2, board, next_cards, x1, y1)
        next_cards[key] = value
        board[x1][y1], board[x2][y2] = key, key


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r, c = 1, 0
print(solution(board, r, c))
