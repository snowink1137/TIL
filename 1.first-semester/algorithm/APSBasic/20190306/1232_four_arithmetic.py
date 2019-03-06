import sys

sys.stdin = open('1232_input.txt', 'r')

for test_case in range(1, 11):
    N = int(input())

    arr = [0] * (N + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)

    for _ in range(N):
        temp = input().split()
        length = len(temp)
        idx = int(temp[0])

        if length == 2:
            arr[idx] = int(temp[1])
        else:
            arr[idx] = temp[1]
            L[idx] = int(temp[2])
            R[idx] = int(temp[3])

    for i in range(N, 0, -1):
        if arr[i] == '+':
            arr[i] = arr[L[i]] + arr[R[i]]
        elif arr[i] == '-':
            arr[i] = arr[L[i]] - arr[R[i]]
        elif arr[i] == '*':
            arr[i] = arr[L[i]] * arr[R[i]]
        elif arr[i] == '/':
            arr[i] = arr[L[i]] / arr[R[i]]

    print('#{} {}'.format(test_case, int(arr[1])))
