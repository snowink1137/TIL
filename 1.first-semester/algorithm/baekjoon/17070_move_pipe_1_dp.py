import sys

sys.stdin = open('17070.txt', 'r')

dx = (0, 1, 1)
dy = (1, 1, 0)
directions = (1, 2, 3)

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(tuple(map(int, input().split())))

memo = [[0 for _ in range(N)] for _ in range(N)]
memo[0][1] = 1
for i in range(N):
    for j in range(1, N):



result = 0
bfs(0, 1, 1)

print(result)
