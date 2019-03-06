import sys


sys.stdin = open('2115_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    possible = []
    for i in range(N):
        for j in range(N-M+1):
            temp = 0
            temp_list = []
            for k in range(M):
                temp += matrix[i][j+k]
                temp_list.append([i, j+k])

            possible.append(temp_list)

    # print(possible)
    area_best_possible = []
    for area in possible:
        max_sum = 0
        best_possible = 0
        for i in range(1, 2**M):
            temp_list = []
            for j in range(M):
                if i & (1 << j):
                    temp_list.append(area[M-1-j])

            temp_sum = 0
            for temp in temp_list:
                temp_sum += matrix[temp[0]][temp[1]]
                if temp_sum > C:
                    temp_sum -= matrix[temp[0]][temp[1]]
                    break

            if temp_sum > max_sum:
                max_sum = temp_sum
                best_possible = temp_list

        area_best_possible.append(best_possible)

    # print(area_best_possible)
    length = len(area_best_possible)
    area_best_possible_no_repeat = []
    for i in range(1, 2 ** length):
        temp_list = []
        for j in range(length):
            if i & (1 << j):
                temp_list.append(area_best_possible[length-1-j])

        if len(temp_list) == 2:
            for temp in temp_list[0]:
                if temp in temp_list[1]:
                    break
            else:
                area_best_possible_no_repeat.append(temp_list)
    print(area_best_possible_no_repeat)