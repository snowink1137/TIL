import sys

sys.stdin = open('5207.txt', 'r')


def binary_search(n):
    global cnt

    l = 0
    r = len(A) - 1

    left_flag = False
    right_flag = False
    m = (l + r) // 2
    if n == A[m]:
        cnt += 1
        return
    elif n > A[m]:
        right_flag = True
        l = m + 1
    else:
        left_flag = True
        r = m - 1

    while l <= r:
        m = (l + r) // 2

        if n == A[m]:
            cnt += 1
            return
        elif n > A[m]:
            if left_flag:
                right_flag = True
                left_flag = False
                l = m + 1
            else:
                return
        else:
            if right_flag:
                left_flag = True
                right_flag = False
                r = m - 1
            else:
                return


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for b in B:
        binary_search(b)

    print('#{} {}'.format(test_case, cnt))
