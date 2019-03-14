import sys

sys.stdin = open('1475.txt', 'r')

N = int(input())

numbers = [0 for _ in range(10)]
while True:
    if 0 <= N <= 9:
        numbers[N] += 1
        break

    N, b = divmod(N, 10)
    numbers[b] += 1

max_num = max(numbers[0:6] + numbers[7:9])
difference = abs(numbers[6]-numbers[9])
if numbers[6] > numbers[9]:
    if difference % 2:
        temp = (difference // 2) + 1 + numbers[9]
    else:
        temp = difference // 2 + numbers[9]
else:
    if difference % 2:
        temp = (difference // 2) + 1 + numbers[6]
    else:
        temp = difference // 2 + numbers[6]

result = max(temp, max_num)
print(result)
