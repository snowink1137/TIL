import sys

sys.stdin = open('5122.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())

    sequence = list(map(int, input().split()))

    for _ in range(M):
        temp = input().split()

        if temp[0] == 'I':
            sequence.insert(int(temp[1]), temp[2])
        elif temp[0] == 'D':
            sequence.pop(int(temp[1]))
        else:
            sequence[int(temp[1])] = temp[2]

    result = -1
    if len(sequence)-1 >= L:
        result = sequence[L]

    print('#{} {}'.format(test_case, result))
