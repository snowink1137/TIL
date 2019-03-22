import sys

sys.stdin = open('1865.txt', 'r')


def perm(n, k):
    if k == n:
        perm_list.append(arr)
        return

    for i in range(k, n):
        arr[k], arr[i] = arr[i], arr[k]
        perm(n, k+1)
        arr[k], arr[i] = arr[i], arr[k]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    perm_list = []
    arr = [x for x in range(N)]
    perm(N-1, 0)

    print(perm_list)

    min_probability = -1
