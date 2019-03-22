import sys

sys.stdin = open('1865.txt', 'r')


def calculate(n, k=0, acc=1.0):
    global max_probability

    if acc <= max_probability:
        return

    if n == k:
        max_probability = acc
        return

    for i in range(N):
        if not visit[i]:
            new_acc = acc * matrix[k][i]

            visit[i] = True
            calculate(n, k+1, new_acc)
            visit[i] = False


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(lambda x: int(x)*0.01, input().split())))

    visit = [False for _ in range(N)]

    max_probability = 0
    calculate(N)
    print('#{} {}'.format(test_case, format(max_probability*100, '.6f')))

