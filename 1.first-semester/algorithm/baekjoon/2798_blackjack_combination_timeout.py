import sys


sys.stdin = open('2798.txt', 'r')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

index = [x for x in range(N)]
combinations = []
for i in range(2 ** N):
    combination_temp = []
    cnt = 0
    for j in range(N):
        if i & (1 << j):
            combination_temp.append(index[N-1-j])
            cnt += 1

        if cnt == 4:
            break

    if cnt == 3:
        combinations.append(combination_temp)

result = 0
for combi in combinations:
    temp = cards[combi[0]] + cards[combi[1]] + cards[combi[2]]
    if result < temp <= M:
        result = temp

print(result)
