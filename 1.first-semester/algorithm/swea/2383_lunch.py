import sys
from collections import deque

sys.stdin = open('2383.txt', 'r')


def calculate(people_index, stair):
    l = len(people_index)
    calculate_list = [0] * l
    time = 0

    if stair == 1:
        x = stair1[0]
        y = stair1[1]
        k = stair1[2]
    else:
        x = stair2[0]
        y = stair2[1]
        k = stair2[2]

    for i in range(l):
        calculate_list[i] = abs(people[people_index[i]][0]-x) + abs(people[people_index[i]][1]-y)

    calculate_list.sort()
    time = calculate_list[0]
    for i in range(l):
        calculate_list[i] -= time


    queue = deque(calculate_list)
    wait_queue_1 = deque()
    wait_queue_2 = deque()
    wait_queue_3 = deque()
    flow = 0
    time_table = [0, 0, 0]
    while len(queue):
        if time

        if len(wait_queue_1) == 0:
            if queue


    return time

def go(number, depth=0, select=0):
    global result

    if depth == number-1:
        use_stair1 = []
        use_stair2 = []
        for j in range(number):
            if select & (1 << j):
                use_stair1.append(j)
            else:
                use_stair2.append(j)

        temp1 = calculate(use_stair1, 1)
        temp2 = calculate(use_stair2, 2)

        result = max(temp1, temp2)

    for i in range(number):
        go(number, depth+1, select|1<<i)
        go(number, depth+1, select)




T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [tuple(map(int, input().split())) for _ in range(N)]

    people = []
    stair1 = ()
    stair2 = ()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                continue
            elif matrix[i][j] == 1:
                people.append((i, j))
            else:
                if stair1:
                    stair2 = (i, j, matrix[i][j])
                else:
                    stair1 = (i, j, matrix[i][j])

    result = 0xffffff
    go(len(people))
    print('#{} {}'.format(test_case, result))

