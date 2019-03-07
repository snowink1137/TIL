import sys

sys.stdin = open('8979.txt', 'r')

N, K = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


matrix.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

memo = 0
for i in range(len(matrix)):
    if matrix[i][0] == K:
        memo = i
        break

result = 0
for i in range(len(matrix)):
    if matrix[i][1:] == matrix[memo][1:]:
        result = i + 1
        break

print(result)