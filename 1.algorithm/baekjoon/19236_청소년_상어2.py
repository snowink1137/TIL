# 자료: 물고기 정보(번호, 위치, 방향), 방향 정보(8가지 방향, 회전에 따른 순서로), 상어 정보(위치, 방향)
# 기능: 물고기 이동, 상어 이동(다양한 경우를 재귀로 구현)

from copy import deepcopy
import sys

sys.stdin = open('19236_sample_input.txt', 'r')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def next(fish_info, shark):
    new_xy_list = []
    shark_x = shark['location'][0]
    shark_y = shark['location'][1]
    shark_direction = shark['direction']

    for i in range(1, 4):
        shark_new_x = shark_x + dx[shark_direction] * i
        shark_new_y = shark_y + dy[shark_direction] * i

        if not (0 <= shark_new_x < 4 and 0 <= shark_new_y < 4):
            continue

        if not fish_info[(shark_new_x, shark_new_y)]:
            continue

        new_xy_list.append((shark_new_x, shark_new_y))

    return new_xy_list


def move(fish_map, fish_info, shark):
    for fish_number in sorted(fish_map.keys()):
        x, y = fish_map[fish_number]
        direction = fish_info[(x, y)]['direction']

        for i in range(8):
            new_x = x + dx[(direction+i)%8]
            new_y = y + dy[(direction+i)%8]

            if not (0 <= new_x < 4 and 0 <= new_y < 4):
                continue

            if shark['location'] == (new_x, new_y):
                continue

            if fish_info[(new_x, new_y)]:
                fish_map[fish_info[(x, y)]['number']], fish_map[fish_info[(new_x, new_y)]['number']] = fish_map[fish_info[(new_x, new_y)]['number']], fish_map[fish_info[(x, y)]['number']]
                fish_info[(x, y)], fish_info[(new_x, new_y)] = fish_info[(new_x, new_y)], fish_info[(x, y)]
                break
            else:
                fish_map[fish_number] = (new_x, new_y)
                fish_info[(new_x, new_y)] = fish_info[(x, y)]
                fish_info[(x, y)] = None
                break


def dfs(result_mid, fish_map, fish_info, shark):
    global result
    fish_map = deepcopy(fish_map)
    fish_info = deepcopy(fish_info)
    shark = deepcopy(shark)

    # 물고기 먹기
    fish_number = fish_info[shark['location']]['number']
    fish_direction = fish_info[shark['location']]['direction']
    fish_map.pop(fish_info[shark['location']]['number'])
    fish_info[shark['location']] = None
    shark['direction'] = fish_direction

    # 현재까지 최대 값 탐색
    result = max(result_mid+fish_number, result)

    # 물고기 이동
    move(fish_map, fish_info, shark)

    # 상어 이동
    new_xy_list = next(fish_info, shark)
    for new_x, new_y in new_xy_list:
        next_shark = deepcopy(shark)
        next_shark['location'] = (new_x, new_y)
        dfs(result_mid+fish_number, fish_map, fish_info, next_shark)

    return


fish_info = {}
fish_map = {}
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        fish_info[(i, j)] = {
            'number': temp[j*2],
            'direction': temp[j*2+1]-1,
        }
        fish_map[temp[j*2]] = (i, j)

shark = {
    'location': (0, 0),
    'direction': 0,
}

result = 0
dfs(0, fish_map, fish_info, shark)
print(result)
