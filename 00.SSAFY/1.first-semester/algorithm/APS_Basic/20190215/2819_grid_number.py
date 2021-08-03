import sys


sys.stdin = open('2819_sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    case_matrix = []
    for i in range(4):
        case_matrix.append(list(map(int, input().split())))

    index_list = []
    num_base = [0, 1, 2, 3]
    for i in num_base:
        for j in num_base:
            index_list.append((i, j))

    possible_list = {}
    for index in index_list:
        temp_list = []
        if index[0] - 1 >= 0:
            temp_list.append((index[0]-1, index[1]))

        if index[0] + 1 <= 3:
            temp_list.append((index[0]+1, index[1]))

        if index[1] - 1 >= 0:
            temp_list.append((index[0], index[1]-1))

        if index[1] + 1 <= 3:
            temp_list.append((index[0], index[1]+1))

        possible_list[index] = temp_list

    result_list = []
    for i in index_list:
        for j in possible_list[i]:
            for k in possible_list[j]:
                for l in possible_list[k]:
                    for m in possible_list[l]:
                        for n in possible_list[m]:
                            for o in possible_list[n]:
                                result = '' + str(case_matrix[i[0]][i[1]]) + str(case_matrix[j[0]][j[1]])  + str(case_matrix[k[0]][k[1]]) + str(case_matrix[l[0]][l[1]]) + str(case_matrix[m[0]][m[1]]) + str(case_matrix[n[0]][n[1]]) + str(case_matrix[o[0]][o[1]])
                                if result in result_list:
                                    continue
                                else:
                                    result_list.append(result)

    print(f'#{test_case} {len(result_list)}')




