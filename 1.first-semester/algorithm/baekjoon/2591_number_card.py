import sys

sys.stdin = open('2591.txt', 'r')

numbers = list(map(int, list(input())))
numbers.insert(0, 0)
N = len(numbers)
memo = [0] * 41
memo[1] = 1
check = N

for i in range(2, N):
    if numbers[i] > 0:
        memo[i] += memo[i-1]

    if 10 <= 10 * numbers[i-1] + numbers[i] <= 34:
        memo[i] += memo[i-2]
        if numbers[i-1] == 0:
            check -= 1

print(memo[check])
