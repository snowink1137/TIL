import sys

sys.stdin = open('5097_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))
    index = M % N

    print('#{} {}'.format(test_case, numbers[index]))
