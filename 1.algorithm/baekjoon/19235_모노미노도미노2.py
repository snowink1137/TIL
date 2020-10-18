import sys

sys.stdin = open('19235_sample_input.txt', 'r')

n = int(input())
score = 0

# 녹색 보드판과 파란색 보드판을 선언합니다.
greenboard = [[0] * 4 for _ in range(6)]
blueboard = [[0] * 4 for _ in range(6)]

# 각 열(y)마다 얼만큼 낮은 칸까지 떨어질 수 있는지 체크하는 서브함수입니다.
def dropblock(ny, board):
    nx = -1
    while 1:
        nx += 1
        if nx == 6:
            nx -= 1
            break
        elif board[nx][ny]:
            nx -= 1
            break
    return nx

# nx,ny에 있는 블럭이 최대 얼마나 낮게 떨어질 수 있는지 높이를 반환하는 서브함수입니다.
def dropblock2(ny, nx, board):
    while 1:
        nx += 1
        if nx == 6:
            nx -= 1
            break
        elif board[nx][ny]:
            nx -= 1
            break
    return nx

# 한줄이 꽉 찼을 때 블록을 떨어뜨리는 서브함수입니다.
def down(board):
    visit = {}
    for h in range(4, -1, -1):
        for w in range(4):
            if visit.get((h, w)) is None and board[h][w]:
                if w < 3 and board[h][w] == board[h][w + 1]:
                    min1 = dropblock2(w, h, board)
                    min2 = dropblock2(w+1, h, board)
                    min3 = min(min1, min2)
                    if min3 != h:
                        board[min3][w] = board[h][w]
                        board[min3][w + 1] = board[h][w + 1]
                        board[h][w] = 0
                        board[h][w + 1] = 0
                    visit[(h, w)] = 1
                    visit[(h, w + 1)] = 1
                else:
                    visit[(h, w)] = 1
                    idx = dropblock2(w, h, board)
                    if idx != h:
                        board[idx][w] = board[h][w]
                        board[h][w] = 0

# 보드의 점수를 체크하여 한줄이 꽉차면 점수를 채우고 블록을 떨어뜨리는 서브함수입니다.
def scorecheck(board):
    global score
    flag = 0
    for row in range(5, 1, -1):
        count = 0
        for w in range(4):
            if board[row][w]:
                count += 1
        if count == 4:
            score += 1
            for w in range(4):
                board[row][w] = 0
            flag = 1
    if flag:
        down(board)
        scorecheck(board)

# 가장 상단의 보드 2줄에 블록이 있을 경우, 하단의 블록들을 없애고 블록전체를 떨어뜨리는 서브함수입니다.
def cleanboard(board):
    count = 0
    for h in range(2):
        if sum(board[h]) > 0:
            count += 1
    for _ in range(count):
        for j in range(4):
            for i in range(5, 0, -1):
                board[i][j] = board[i - 1][j]
            board[0][j] = 0

# 메인함수입니다. 매 블록을 떨어뜨릴 때마다 위의 서브함수들을 사용하여 블록들을 천천히 쌓아올립니다.
for time in range(1, n + 1):
    t, x, y = map(int, input().split())
    if t == 1:
        ng = dropblock(y, greenboard)
        print(ng)
        greenboard[ng][y] = time
        nb = dropblock(x, blueboard)
        blueboard[nb][x] = time
    elif t == 2:
        ng1 = dropblock(y, greenboard)
        ng2 = dropblock(y + 1, greenboard)
        ng = min(ng1, ng2)
        greenboard[ng][y] = time
        greenboard[ng][y + 1] = time
        nb = dropblock(x, blueboard)
        blueboard[nb][x] = time
        nb = dropblock(x, blueboard)
        blueboard[nb][x] = time
    else:
        nb1 = dropblock(x, blueboard)
        nb2 = dropblock(x + 1, blueboard)
        nb = min(nb1, nb2)
        blueboard[nb][x] = time
        blueboard[nb][x + 1] = time
        ng = dropblock(y, greenboard)
        greenboard[ng][y] = time
        ng = dropblock(y, greenboard)
        greenboard[ng][y] = time

    scorecheck(greenboard)
    scorecheck(blueboard)
    cleanboard(greenboard)
    cleanboard(blueboard)
# 각 보드판마다 블록 개수를 카운트할 변수 b,g를 선언합니다.
b = 0
g = 0
for i in range(6):
    for j in range(4):
        if greenboard[i][j]:
            g += 1
        if blueboard[i][j]:
            b += 1
# 최종 점수와 초록색 보드판의 블록 개수와 파란색 보드판의 블록 개수를 출력합니다.
print(score)
print(b + g)