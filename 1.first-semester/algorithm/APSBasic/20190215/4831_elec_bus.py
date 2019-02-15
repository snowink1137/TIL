import sys


sys.stdin = open('4831_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    find = False
    K, N, M = tuple(map(int, input().split()))
    charge_station_list = [0]
    charge_station_list += list(map(int, input().split()))
    charge_station_list += [N]

    distance_list = []
    for i in range(len(charge_station_list)-1):
        distance = charge_station_list[i+1] - charge_station_list[i]
        if distance > K:
            print(f'#{test_case} 0')
            find = True
        else:
            distance_list.append(distance)

    if find:
        continue

    optimize_num = 0
    judge_temp = 0
    for i in range(len(distance_list)):
        judge_temp += distance_list[i]
        if judge_temp > K:
            optimize_num += 1
            judge_temp = distance_list[i]

    print(f'#{test_case} {optimize_num}')
