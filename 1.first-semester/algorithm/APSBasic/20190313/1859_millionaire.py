import sys

sys.stdin = open('1859.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    information = list(map(int, input().split()))

    profit = 0
    max_price = information[N-1]
    for i in range(N-2, -1, -1):
        info = information[i]
        if info > max_price:
            max_price = information[i]
        else:
            profit += max_price - info

    print('#{} {}'.format(test_case, profit))
