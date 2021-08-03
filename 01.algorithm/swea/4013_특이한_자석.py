import sys
from collections import deque

sys.stdin = open('4013_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    result = 0
    K = int(input())
    wheel_0 = deque(list(map(int, input().split())))
    wheel_1 = deque(list(map(int, input().split())))
    wheel_2 = deque(list(map(int, input().split())))
    wheel_3 = deque(list(map(int, input().split())))
    wheels = [wheel_0, wheel_1, wheel_2, wheel_3]

    spin_info = [list(map(int, input().split())) for _ in range(K)]
    for spin in spin_info:
        # 돌아야 하는지 체크
        targets = [False, False, False, False]
        targets[spin[0]-1] = spin[1]

        before_idx = spin[0] - 1
        left_idx = spin[0] - 1 - 1
        while 0 <= left_idx < 4:
            if not targets[before_idx]:
                break

            if wheels[before_idx][6] == wheels[left_idx][2]:
                break

            if targets[before_idx] == -1:
                targets[left_idx] = 1
            else:
                targets[left_idx] = -1

            before_idx = left_idx
            left_idx -= 1

        before_idx = spin[0] - 1
        right_idx = spin[0] - 1 + 1
        while 0 <= right_idx < 4:
            if not targets[before_idx]:
                break

            if wheels[before_idx][2] == wheels[right_idx][6]:
                break

            if targets[before_idx] == -1:
                targets[right_idx] = 1
            else:
                targets[right_idx] = -1

            before_idx = right_idx
            right_idx += 1

        # 돌리기
        for target_idx in range(len(targets)):
            direction = targets[target_idx]
            if direction == 1:
                wheels[target_idx].rotate(1)
            elif direction == -1:
                wheels[target_idx].rotate(-1)

    # 점수 체크
    for wheel_idx in range(len(wheels)):
        if wheels[wheel_idx][0]:
            result += 2 ** wheel_idx

    print('#{} {}'.format(test_case, result))
