import sys

sys.stdin = open('20058_sample_input.txt', 'r')


def dfs(x, y, cnt):
    global N, result2

    for d in directions:
        new_x, new_y = x + d[0] ,y + d[1]
        if 0 <= new_x < 2**N and 0 <= new_y < 2**N and ice_map[new_x][new_y] and not visit[new_x][new_y]:
            if result2 < cnt+1:
                result2 = cnt+1

            visit[new_x][new_y] = True
            dfs(new_x, new_y, cnt+1)


directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

result1 = 0
result2 = 0

N, Q = map(int, input().split())

ice_map = []
for i in range(2**N):
    ice_map.append(list(map(int, input().split())))

firestorms = list(map(int, input().split()))
for L in firestorms:
    # 회전. https://m.blog.naver.com/pasdfq/222120359076 그림 참고
    step = 2 ** L
    for i in range(0, 2**N, step):
        for j in range(0, 2**N, step):
            temp = []
            for k in range(i, i+step):
                temp.append(ice_map[k][j:j+step])

            for x in range(step):
                for y in range(step):
                    ice_map[i+y][j+step-1-x] = temp[x][y]

    # 얼음 세기
    ice_count_map = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for x in range(2**N):
        for y in range(2**N):
            for d in directions:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < 2**N and 0 <= new_y < 2**N and ice_map[new_x][new_y]:
                    ice_count_map[x][y] += 1

    # 얼음 녹이기
    for i in range(2**N):
        for j in range(2**N):
            if ice_map[i][j] and ice_count_map[i][j] < 3:
                ice_map[i][j] -= 1

# 얼음 합
for ice in ice_map:
    result1 += sum(ice)

# 얼음 크기 측정
visit = [[False for _ in range(2**N)] for _ in range(2**N)]
for x in range(2**N):
    for y in range(2**N):
        if ice_map[x][y] and not visit[x][y]:
            dfs(x, y, 0)

print(result1)
print(result2)
