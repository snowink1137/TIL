import sys


sys.stdin = open('2115_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split())

    # 입력 받기
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 조합 만들기
    combinations = []
    numbers = [x for x in range(M)]
    for i in range(1, 2**M):
        temp = []
        for j in range(M):
            if i & (1 << j):
                temp.append(numbers[M-1-j])

        combinations.append(temp)

    # 부분 최대합 구하기
    sum_matrix = [[0] * (N - M + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            temp = matrix[i][j:j+M]
            max_square_sum = 0
            for combi in combinations:
                temp_square_sum = 0
                temp_sum = 0
                for idx in combi:
                    temp_sum += temp[idx]
                    if temp_sum > C:
                        continue

                    temp_square_sum += temp[idx] * temp[idx]

                if temp_square_sum > max_square_sum:
                    max_square_sum = temp_square_sum

            sum_matrix[i][j] = max_square_sum

    # 한 줄에 두 사람 못들어가는 경우
    if 2 * M > N:
        row_max = []
        for i in range(N):
            row_max.append(max(sum_matrix[i]))

        row_max.sort(reverse=True)
        result = row_max[0] + row_max[1]
        print('#{} {}'.format(test_case, result))
    # 한 줄에 두 사람 들어가는 경우
    else:
        # 일단 한 줄에는 한명만 들어간다고 해서 최대로 추측되는 값 고르기(위에서 구했던 것과 같음)
        row_max = []
        for i in range(N):
            row_max.append(max(sum_matrix[i]))

        row_max.sort(reverse=True)
        result = row_max[0] + row_max[1]

        # 혹시 한 줄에 한 명이 들어갈 경우 최대로 추측되는 값과 비교하기 위해 필요한 인덱스 조합 생성
        combinations = []
        numbers = [x for x in range(N - M + 1)]
        for i in range(1, 2 ** (N - M + 1)):
            temp = []
            cnt = 0
            for j in range(N - M + 1):
                if i & (1 << j):
                    temp.append(numbers[N - M + 1 - 1 - j])
                    cnt += 1
                if cnt == 3:
                    break
            else:
                if cnt != 2:
                    continue
                if abs(temp[0] - temp[1]) > M - 1:
                    combinations.append(temp)
                else:
                    continue

        # 각 줄 별로 생성한 인덱스 조합으로 최대로 추측되는 값보다 큰지 체크. 만약 크다면 result 교체
        for i in range(N):
            temp = sorted(sum_matrix[i][:])
            if temp[0] + temp[1] < result:
                continue
            else:
                for combi in combinations:
                    if sum_matrix[i][combi[0]] + sum_matrix[i][combi[1]] < result:
                        continue
                    else:
                        result = sum_matrix[i][combi[0]] + sum_matrix[i][combi[1]]

        print('#{} {}'.format(test_case, result))
