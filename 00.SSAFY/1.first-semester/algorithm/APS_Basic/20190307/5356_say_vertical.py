import sys


sys.stdin = open('5356_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    matrix = [['*'] * 15 for _ in range(5)]

    for i in range(5):
        row_temp = input()
        length = len(row_temp)

        for j in range(length):
            matrix[i][j] = row_temp[j]

    result = ''
    for j in range(15):
        for i in range(5):
            temp = matrix[i][j]
            if temp == '*':
                continue
            result += temp

    print('#{} {}'.format(test_case, result))
