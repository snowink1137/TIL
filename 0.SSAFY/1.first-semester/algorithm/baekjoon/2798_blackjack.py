import sys

sys.stdin = open('2798.txt', 'r')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
result = 0
for i in range(N):
    if cards[i] > M:
        continue
    for j in range(i + 1, N):
        if cards[i] + cards[j] >= M:
            continue
        for k in range(j + 1, N):
            if result < cards[i] + cards[j] + cards[k] <= M:
                result = cards[i] + cards[j] + cards[k]

print(result)
