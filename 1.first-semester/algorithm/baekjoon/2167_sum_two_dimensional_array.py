import sys

sys.stdin = open('2167.txt', 'r')

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())

    result = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            result += matrix[a][b]

    print(result)
