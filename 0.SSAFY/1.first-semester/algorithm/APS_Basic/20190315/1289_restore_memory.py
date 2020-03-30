import sys

sys.stdin = open('1289.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    bits = list(map(int, input()))

    pre = bits[0]
    if pre == 1:
        cnt = 1
    else:
        cnt = 0

    for i in range(1, len(bits)):
        if pre == bits[i]:
            continue
        else:
            pre = bits[i]
            cnt += 1

    print('#{} {}'.format(test_case, cnt))
