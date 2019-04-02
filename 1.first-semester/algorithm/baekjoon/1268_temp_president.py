import sys

sys.stdin = open('1268.txt', 'r')

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
class_note = [[[False for _ in range(9)] for _ in range(5)] for _ in range(N)]

for i in range(N):
    for j in range(5):
        class_note[i][j][matrix[i][j]-1] = True

result = 0
result_index = 0
for i in range(N):
    temp = set()
    for ii in range(N):
        if i == ii:
            continue

        for j in range(5):
            for k in range(9):
                if class_note[i][j][k] and class_note[ii][j][k]:
                    temp.add(ii)

    t = len(temp)
    if t > result:
        result = t
        result_index = i

print(result_index+1)
