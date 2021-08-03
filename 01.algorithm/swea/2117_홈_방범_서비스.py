import sys

sys.stdin = open('2117_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    map_matrix = [list(map(int, input().split())) for _ in range(N)]

    home_index = []
    for i in range(N):
        for j in range(N):
            if map_matrix[i][j]:
                home_index.append([i, j])

    for k in range(N+1, 0, -1):
        flag = False
        temp_result = 0
        for i in range(N):
            for j in range(N):
                cnt = 0
                for home in home_index:
                    if abs(i-home[0]) + abs(j-home[1]) < k:
                        cnt += 1

                if cnt * M - (k * k + (k-1) * (k-1)) >= 0:
                    flag = True
                    if cnt > temp_result:
                        temp_result = cnt

        if flag:
            result = temp_result
            break

    print('#{} {}'.format(test_case, result))
