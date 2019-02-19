import sys


sys.stdin = open('4836_sample_input.txt')
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    information = []
    for row in range(N):
        information.append(list(map(int, input().split())))

    red_set = []
    blue_set = []
    for info in information:
        if info[4] == 1:
            for i in range(info[0], info[2]+1):
                for j in range(info[1], info[3]+1):
                    red_set.append([i, j])
        else:
            for i in range(info[0], info[2]+1):
                for j in range(info[1], info[3]+1):
                    blue_set.append([i, j])

    cnt = 0
    for red in red_set:
        for blue in blue_set:
            if red == blue:
                cnt += 1

    print(f'#{test_case} {cnt}')
