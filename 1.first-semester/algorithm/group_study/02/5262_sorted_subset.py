import sys

sys.stdin = open('5262_sample_input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    information = list(map(int, input().split()))

    N = information[0]
    numbers = information[1:]

    result = 1
    for k in range(N, 1, -1):
        combinations = []
        bits = [0] * k
        subset(N-k, N)


    print(f'#{test_case} {result}')