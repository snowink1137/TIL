import sys

sys.stdin = open('5162.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    A, B, C = map(int, input().split())

    if A > B:
        result = C // B
    else:
        result = C // A

    print('#{} {}'.format(test_case, result))
