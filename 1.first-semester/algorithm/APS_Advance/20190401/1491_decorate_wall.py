import sys

sys.stdin = open('1491.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, A, B = map(int, input().split())

    result = 10**1000
    for i in range(N):
        R = 1
        C = 1 + i
        while True:
            n = R * C
            if n <= N:
                temp_result = (A * i) + (B * (N - n))
                if temp_result < result:
                    result = temp_result

            else:
                break

            R += 1
            C += 1

    print('#{} {}'.format(test_case, result))
