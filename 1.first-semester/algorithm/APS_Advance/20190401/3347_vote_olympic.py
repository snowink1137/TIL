import sys

sys.stdin = open('3347.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    votes = [0] * (N+1)

    for b in B:
        cnt = 0
        while True:
            if A[cnt] <= b:
                votes[cnt] += 1
                break

            cnt += 1

    print('#{} {}'.format(test_case, votes.index(max(votes)) + 1))
