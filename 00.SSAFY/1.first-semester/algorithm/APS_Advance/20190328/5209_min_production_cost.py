import sys

sys.stdin = open('5209.txt', 'r')


def check(N, depth=0, use=0, acc=0):
    global min_cost
    if acc >= min_cost:
        return

    if N == depth:
        min_cost = acc
        return

    for i in range(N):
        if not use & (1 << i):
            check(N, depth+1, use | (1 << i), acc+(matrix[depth][i]))


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = tuple(tuple(map(int, input().split())) for i in range(N))

    min_cost = N * N * 99
    check(N)
    print('#{} {}'.format(test_case, min_cost))

