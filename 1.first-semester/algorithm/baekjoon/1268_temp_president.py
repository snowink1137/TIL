import sys

sys.stdin = open('1268.txt', 'r')

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

count_matrix = [[[0 for _ in range(10)] for _ in range(5)] for _ in range(N)]

for i in range(N):
    for j in range(5):
        class_num = matrix[i][j] - 1
        for k in range(N):
            count_matrix[k][j][class_num] += 1

result = 0
result_index = 0
for i in range(N):
    temp = 0
    for j in range(5):
        for k in range(10):
            temp += count_matrix[i][j][k]

    if temp > result:
        result = temp
        result_index = i

print(i+1)
