import sys

sys.stdin = open('2294.txt', 'r')

n, k = map(int, input().split())

coin_type = set()
for _ in range(n):
    coin_type.add(int(input()))

coin_list = list(coin_type)
coin_list.sort()
max_num = max(coin_list[-1], k)
memo = [0] * (max_num + 1)

for i in coin_list:
    memo[i] = 1
    for j in range(i+1, max_num+1):
        if memo[j-i]:
            temp = memo[j-i] + 1
            if memo[j] == 0:
                memo[j] = temp
            elif temp < memo[j]:
                memo[j] = temp

if memo[k] == 0:
    result = -1
else:
    result = memo[k]

print(result)
