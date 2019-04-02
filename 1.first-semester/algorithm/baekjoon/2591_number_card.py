import sys

sys.stdin = open('2591.txt', 'r')

numbers = list(map(int, list(input())))
N = len(numbers)
memo = [0] * (N+1)
memo[1] = 1
flag = False
if N > 1:
    memo[2] = 2
    for i in range(3, N+1):
        memo[i] = memo[i-1] + memo[i-2]

    result = 1
    cnt = 1
    for i in range(N-1):
        if numbers[i] == 0 or numbers[i+1] == 0:
            flag = True
            break

        if numbers[i]*10 + numbers[i+1] <= 34:
            cnt += 1
        else:
            result *= memo[cnt]
            cnt = 1

    if flag:
        print(0)
    else:
        result *= memo[cnt]
        print(result)
else:
    print(1)