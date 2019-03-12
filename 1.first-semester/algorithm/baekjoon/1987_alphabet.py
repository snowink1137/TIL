import sys

sys.stdin = open('1987.txt', 'r')


def dfs(x, y, cnt):
    global max_cnt
    if visit[information[x][y]]:
        if cnt-1 > max_cnt:
            max_cnt = cnt-1
        return

    visit[information[x][y]] = True
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if not 0 <= new_x <= R - 1 or not 0 <= new_y <= C - 1:
            continue
        dfs(new_x, new_y, cnt+1)

    visit[information[x][y]] = False


R, C = map(int, input().split())
information = [list(map(lambda x: ord(x)-65, input())) for i in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visit = [0 for _ in range(26)]
max_cnt = 0
dfs(0, 0, 1)
print(max_cnt)
