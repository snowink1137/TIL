import sys

sys.stdin = open('2591.txt', 'r')

numbers = list(map(int, list(input())))
N = len(numbers)
memo = [0] * (N+1)
memo[0] = 1
memo[1] = 1

for i in range(1, N):
    if numbers[i] > 0:
        memo[i+1] += memo[i]

    if 10 <= 10 * numbers[i-1] + numbers[i] <= 34:
        memo[i+1] += memo[i-1]

print(memo[N])
