import sys


sys.stdin = open('4835_sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = tuple(map(int, input().split()))

    arr = list(map(int, input().split()))

    sum_list = []
    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += arr[i+j]

        if i == 0:
            max_sum = temp
            min_sum = temp

        if temp > max_sum:
            max_sum = temp
        elif temp < min_sum:
            min_sum = temp

    print(f'#{test_case} {max_sum-min_sum}')
