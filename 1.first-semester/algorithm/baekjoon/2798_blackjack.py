import sys

sys.stdin = open('2798.txt', 'r')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
length = len(cards)
result = 0
flag = False
for i in range(N):
    if cards[i] > M:
        continue
    for j in range(i + 1, N):
        if cards[i] + cards[j] > M:
            continue
        for k in range(j + 1, N):
            if cards[i] + cards[j] + cards[k] <= M:
                result = cards[i] + cards[j] + cards[k]
                flag = True
                break

        if flag:
            break

    if flag:
        break

print(result)
