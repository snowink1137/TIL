import sys

sys.stdin = open('2805.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input())))

    harvest = 0
    flag = True
    for i in range(N):
        if flag:
            for j in range((N // 2) - i, (N//2) + i + 1):
                harvest += matrix[i][j]
                if i == (N // 2):
                    flag = False
        else:
            for j in range(i - (N // 2), N + (N // 2) - i):
                harvest += matrix[i][j]

    print('#{} {}'.format(test_case, harvest))
