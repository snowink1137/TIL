import sys

sys.stdin = open('1974.txt')

T = int(input())
for test_case in range(1, T + 1):
    matrix = []
    for _ in range(9):
        matrix.append(list(map(int, input().split())))

    result = 1
    flag = False
    for i in range(9):
        row_list = []
        column_list = []
        for j in range(9):
            row_element = matrix[i][j]
            column_element = matrix[j][i]
            if row_element not in row_list:
                row_list.append(matrix[i][j])
            else:
                flag = True
                result = 0
                break

            if column_element not in column_list:
                column_list.append(matrix[j][i])
            else:
                flag = True
                result = 0
                break

    if flag:
        print('#{} {}'.format(test_case, result))
        continue

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box_list = []
            row = 0
            for ii in range(3):
                for jj in range(3):
                    box_element = matrix[i+ii][j+jj]
                    if box_element not in box_list:
                        box_list.append(box_element)
                    else:
                        flag = True
                        result = 0
                        break

    print('#{} {}'.format(test_case, result))
