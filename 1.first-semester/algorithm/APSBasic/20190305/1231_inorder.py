import sys

sys.stdin = open('1231_input.txt', 'r')


def get_string(v):
    if v == 0:
        return

    get_string(L[v])
    result.append(V[v])
    get_string(R[v])


for test_case in range(1, 11):
    N = int(input())

    L = [0] * (N + 1)
    R = [0] * (N + 1)
    V = [0] * (N + 1)

    for i in range(1, N+1):
        arr = input().split()
        if len(arr) == 4:
            V[i] = arr[1]
            L[i] = int(arr[2])
            R[i] = int(arr[3])
        elif len(arr) == 3:
            V[i] = arr[1]
            L[i] = int(arr[2])
        elif len(arr) == 2:
            V[i] = arr[1]

    result = []
    get_string(1)
    print('#{} {}'.format(test_case, ''.join(result)))
