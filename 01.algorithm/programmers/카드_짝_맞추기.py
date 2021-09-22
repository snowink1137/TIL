# 미완성. 그리디로는 안되는 경우가 있다.
# 첫 번째 카드와 두 번째 카드의 거리가 같을 때, 누구를 먼저 방문하느냐에 따라 그 다음 결과가 달라지는 경우 있음.
# 완탐으로 해야할 것으로 보인다.


from collections import defaultdict, deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def solution(board, r, c):
    answer = 0

    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[board[i][j]].append([i, j])

    for _ in range(len(cards.keys())):
        next_card = 0
        next_card_start_coordinate = [0, 0]
        next_card_end_coordinate = [0, 0]
        min_distance = 9999
        for card, coordinate in cards.items():
            card_distance = 0
            x1, y1 = coordinate[0][0], coordinate[0][1]
            x2, y2 = coordinate[1][0], coordinate[1][1]
            d1 = distance(board, r, c, x1, y1)
            d2 = distance(board, r, c, x2, y2)

            flag = -1
            if d1 < d2:
                card_distance = d1
                flag = 0
            else:
                card_distance = d2
                flag = 1

            if card_distance < min_distance:
                min_distance = card_distance
                next_card = card
                if flag == 0:
                    next_card_start_coordinate = [x1, y1]
                    next_card_end_coordinate = [x2, y2]
                elif flag == 1:
                    next_card_start_coordinate = [x2, y2]
                    next_card_end_coordinate = [x1, y1]

        answer += min_distance + distance(board, next_card_start_coordinate[0], next_card_start_coordinate[1], next_card_end_coordinate[0], next_card_end_coordinate[1])
        answer += 2

        # update
        r = next_card_end_coordinate[0]
        c = next_card_end_coordinate[1]
        board[next_card_start_coordinate[0]][next_card_start_coordinate[1]] = 0
        board[next_card_end_coordinate[0]][next_card_end_coordinate[1]] = 0
        cards.pop(next_card)


    return answer


def distance(board, r, c, input_x, input_y):
    queue = deque()
    queue.append([r, c])
    visit = [[0 for _ in range(4)] for _ in range(4)]

    while queue:
        q = queue.popleft()
        x, y = q[0], q[1],

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if not (0 <= new_x < 4 and 0 <= new_y < 4) or (new_x == r and new_y == c):
                continue

            if visit[new_x][new_y] != 0 and (visit[new_x][new_y] <= visit[x][y] + 1):
                continue

            visit[new_x][new_y] = visit[x][y] + 1
            queue.append([new_x, new_y])

        for i in range(4):
            for t in range(1, 4):
                new_x, new_y = x + dx[i] * t, y + dy[i] * t
                if not (0 <= new_x < 4 and 0 <= new_y < 4) or (new_x == r and new_y == c):
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

            if new_x == r and new_y == c:
                continue

            visit[new_x][new_y] = visit[x][y] + 1
            queue.append([new_x, new_y])

    test = 1
    return visit[input_x][input_y]


board = [[0, 0, 1, 0], [1, 0, 0, 0], [4, 4, 3, 2], [0, 3, 2, 0]]
r, c = 2, 0
print(solution(board, r, c))
