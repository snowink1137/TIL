import sys

sys.stdin = open('4861_sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = tuple(map(int, input().split()))

    case = [[0]*N for _ in range(N)]
    for i in range(N):
        line = input()
        for j in range(N):
            case[i][j] = line[j]

    for t in range(N-M+1):
        for i in range(N):
            for j in range(M):
                if case[i][j+t] != case[i][M-1-j+t]:
                    break
            else:
                print(f'#{test_case} {"".join(case[i][t:t+M])}')

        for j in range(N):
            temp_line = [0] * M
            for i in range(M):
                if case[i+t][j] != case[M-1-i+t][j]:
                    break
                else:
                    temp_line[i] = case[i+t][j]
                    temp_line[M-1-i] = case[i+t][j]
            else:
                temp_line = ''.join(temp_line)
                print(f'#{test_case} {temp_line}')

