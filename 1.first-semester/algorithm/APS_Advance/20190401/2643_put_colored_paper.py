import sys

sys.stdin = open('2643.txt', 'r')

N = int(input())
information = [list(map(int, input().split())) for _ in range(N)]

for info in information:
    if info[0] < info[1]:
        info[1], info[0] = info[0], info[1]

information.sort(key=lambda x: (x[0], x[1]), reverse=True)
D = [1] * N

for i in range(N):
    temp = 0
    for k in range(i):
        if information[k][0] >= information[i][0] and information[k][1] >= information[i][1]:
            if D[k] > temp:
                temp = D[k]

    D[i] = temp + 1

print(max(D))
