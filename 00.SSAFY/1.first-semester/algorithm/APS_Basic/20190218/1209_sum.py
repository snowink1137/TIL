import sys


sys.stdin = open('1209_input.txt', 'r')
for test_case in range(1, 11):
    tc = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    max_sum = 0
    for j in range(100):
        sum_element1 = 0
        sum_element2 = 0
        for i in range(100):
            sum_element1 += matrix[i][j]
            sum_element2 += matrix[j][i]

        if sum_element1 > max_sum:
            max_sum = sum_element1

        if sum_element2 > max_sum:
            max_sum = sum_element2

    sum_element1 = 0
    sum_element2 = 0
    for i in range(100):
        sum_element1 += matrix[i][i]
        sum_element2 += matrix[i][99-i]

    if sum_element1 > max_sum:
        max_sum = sum_element1

    if sum_element2 > max_sum:
        max_sum = sum_element2

    print(f'#{tc} {max_sum}')
