import sys
from collections import deque

sys.stdin = open('5186.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    result = deque()
    cnt = 0
    while cnt >= -12:
        cnt -= 1

        temp = 2 ** cnt

        if N - temp >= 0:
            N -= temp
            result.append(1)
        else:
            result.append(0)
            continue

        if N == 0:
            break

    if N != 0:
        result = 'overflow'
    else:
        result = ''.join(map(str, result))

    print('#{} {}'.format(tc, result))
