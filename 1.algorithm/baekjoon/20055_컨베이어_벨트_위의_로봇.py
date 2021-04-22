from collections import deque
import sys

sys.stdin = open('20055_sample_input.txt', 'r')

N, K = map(int, input().split())
belts = deque(map(int, input().split()))
robot_map = deque([False for _ in range(N)])

cnt = 0
while K > 0:
    cnt += 1
    belts.rotate()
    robot_map.rotate()

    if robot_map[-1]:
        robot_map[-1] = False

    if belts[0]:
        robot_map[0] = True
        belts[0] -= 1
        if belts[0] == 0:
            K -= 1

    for i in range(N-2, 0, -1):
        if not robot_map[i]:
            continue

        new_i = i+1
        if not robot_map[new_i] and belts[new_i]:
            belts[new_i] -= 1
            if belts[new_i] == 0:
                K -= 1

            robot_map[new_i-1] = False
            robot_map[new_i] = True

            if new_i == N - 1:
                robot_map[new_i] = False

    if not robot_map[0] and belts[0]:
        belts[0] -= 1

        if belts[0] == 0:
            K -= 1

        robot_map[0] = True

print(cnt)
