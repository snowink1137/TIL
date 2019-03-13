import sys

sys.stdin = open('2005.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    result = [[1]]
    for i in range(1, N):
        temp = [0 for _ in range(i-1)]
        temp.append(1)
        temp.insert(0, 1)
        for j in range(1, i):
            temp[j] = result[i-1][j-1] + result[i-1][j]

        result.append(temp)

    print('#{}'.format(test_case))
    for i in range(len(result)):
        print(' '.join(map(str, result[i])))
