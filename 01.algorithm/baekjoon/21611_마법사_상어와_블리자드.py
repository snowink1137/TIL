import sys

sys.stdin = open('21611_sample_input.txt', 'r')

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

answer = 0
for command in commands:
    d, s = command[0], command[1]
    destroyed_area = magic(matrix, d, s)

    answer += score(matrix, destroyed_area)

    while destroyed_area:
        move(matrix, destroyed_area)
        destroyed_area = explode(matrix)
        answer += score(matrix, destroyed_area)

    change(matrix)

print(answer)

# 큐, 이차원 배열, 서로 매핑되는 맵을 미리 만들어서 하면 될 것 같다. 큐랑 이차원 배열을 계속 생성해야하는 게 좀 걸리긴 하는데.. 일단 고고
