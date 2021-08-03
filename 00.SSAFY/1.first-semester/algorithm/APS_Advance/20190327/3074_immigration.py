import sys

sys.stdin = open('3074.txt', 'r')


def binary_search(people, min_time, max_time):
    global result

    if max_time-min_time == 1:
        throughput = 0
        for i in range(N):
            throughput += min_time // T[i]

        if throughput == people:
            result = min_time
        else:
            result = max_time

        return

    mid_time = (min_time + max_time) // 2

    throughput = 0
    for i in range(N):
        throughput += mid_time // T[i]

    if throughput >= people:
        binary_search(people, min_time, mid_time)
    else:
        binary_search(people, mid_time, max_time)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    T = [int(input()) for _ in range(N)]
    max_judge_time = T[-1] * M
    min_judge_time = 0
    result = 0

    binary_search(M, min_judge_time, max_judge_time)
    print('#{} {}'.format(test_case, result))
