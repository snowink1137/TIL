import sys

sys.stdin = open('6485.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    information = []
    for _ in range(N):
        information.append(list(map(int, input().split())))

    count = dict()
    for info in information:
        for i in range(info[0], info[1]+1):
            if count.get(i):
                count[i] += 1
            else:
                count[i] = 1

    print('#{} '.format(test_case), end='')

    P = int(input())
    result = []
    for i in range(P):
        C = int(input())
        if count.get(C):
            result.append(str(count[C]))
        else:
            result.append(str(0))

    result = ' '.join(result)

    print(result)
