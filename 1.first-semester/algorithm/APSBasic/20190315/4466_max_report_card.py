import sys

sys.stdin = open('4466.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    scores = list(map(int, input().split()))

    scores.sort(reverse=True)
    result = 0
    for i in range(K):
        result += scores.pop(0)

    print('#{} {}'.format(test_case, result))
