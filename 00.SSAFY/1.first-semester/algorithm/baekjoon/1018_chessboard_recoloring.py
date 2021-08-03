import sys

sys.stdin = open('1018.txt', 'r')

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(input()))

model1 = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
]
model2 = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
]

global_cnt = 64
for l in range(N-7):
    for k in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        for i in range(l, l+8):

            for j in range(k, k+8):
                if matrix[i][j] != model1[i-l][j-k]:
                    cnt1 += 1

            for j in range(k, k+8):
                if matrix[i][j] != model2[i-l][j-k]:
                    cnt2 += 1

        if cnt1 < global_cnt:
            global_cnt = cnt1

        if cnt2 < global_cnt:
            global_cnt = cnt2

print(global_cnt)
