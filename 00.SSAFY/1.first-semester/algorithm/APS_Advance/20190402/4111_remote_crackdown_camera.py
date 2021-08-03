import sys

sys.stdin = open('4111.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    K = int(input())

    index = list(map(int, input().split()))

    if N < K:
        print('#{} {}'.format(test_case, 0))
        continue

    index = list(set(index))
    index.sort()
    coverage = index[-1] - index[0]

    index_difference = [index[i+1] - index[i] for i in range(len(index)-1)]
    index_difference.sort(reverse=True)

    for i in range(K-1):
        coverage -= index_difference[i]

    print('#{} {}'.format(test_case, coverage))
