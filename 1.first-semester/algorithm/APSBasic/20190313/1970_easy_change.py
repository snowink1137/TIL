import sys

sys.stdin = open('1970.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    a, N = divmod(N, 50000)
    b, N = divmod(N, 10000)
    c, N = divmod(N, 5000)
    d, N = divmod(N, 1000)
    e, N = divmod(N, 500)
    f, N = divmod(N, 100)
    g, N = divmod(N, 50)
    h, N = divmod(N, 10)

    print('#{}'.format(test_case))
    print(a, b, c, d, e, f, g, h)
