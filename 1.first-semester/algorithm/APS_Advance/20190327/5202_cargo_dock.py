import sys

sys.stdin = open('5202.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    forms = [list(map(int, input().split())) for _ in range(N)]

    forms.sort(key=lambda x: x[1])

    cnt = 0
    start = 0
    end = 0
    for form in forms:
        if form[0] >= end:
            cnt += 1
            start = form[0]
            end = form[1]

    print('#{} {}'.format(test_case, cnt))
