import sys

sys.stdin = open('4837_sample_input.txt')
T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for test_case in range(1, T + 1):
    N, K = tuple(map(int, input().split()))
    result = 0
    for i in range(1 << 12):
        temp = 0
        temp_sum = 0
        for j in range(12):
            if temp < K:
                if i & (1 << j):
                    temp += 1
                    temp_sum += A[11-j]
            else:
                break
        else:
            if temp == N and temp_sum == K:
                result += 1

    print(f'#{test_case} {result}')
