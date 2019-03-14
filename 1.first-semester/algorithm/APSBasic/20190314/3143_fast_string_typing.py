import sys

sys.stdin = open('3143.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)

    end = a - b + 1
    i = 0
    cnt = 0
    while i < end:
        j = 0
        while j < b:
            if A[i+j] != B[j]:
                break

            j += 1

        if j == b:
            cnt += 1
            i += j - 1
        else:
            i += 1

    result = a - (cnt * b) + cnt

    print('#{} {}'.format(test_case, result))
