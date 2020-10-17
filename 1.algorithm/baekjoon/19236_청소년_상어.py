# 자료: 물고기 정보(번호, 위치, 방향), 방향 정보(8가지 방향, 회전에 따른 순서로), 상어 정보(위치, 방향)
# 기능: 물고기 이동, 상어 이동(다양한 경우를 재귀로 구현)

import sys

sys.stdin = open('19236_sample_input.txt', 'r')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(result_mid):
    global result, fish_info, fish_map, shark

    if len(fish_map) == 0:
        if result_mid > result:
            result = result_mid

        return

    # 자료 복사
    fish_info_temp = {}
    fish_map_temp = {}
    for k, v in fish_info.items():
        if v == None:
            fish_info_temp[k] = None
            continue

        fish_info_temp[k] = {}
        for kk, vv in v.items():
            fish_info_temp[k][kk] = vv

        fish_map_temp[fish_info_temp[k]['number']] = k

    shark_temp = {
        'location': (shark['location'][0], shark['location'][1]),
        'direction': shark['direction'],
    }
    result_mid_temp = result_mid

    # 물고기 이동
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

    # 상어 이동
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

        result_mid += fish_info[(shark_new_x, shark_new_y)]['number']
        shark['location'] = (shark_new_x, shark_new_y)
        shark['direction'] = fish_info[(shark_new_x, shark_new_y)]['direction']
        fish_map.pop(fish_info[(shark_new_x, shark_new_y)]['number'])
        fish_info[(shark_new_x, shark_new_y)] = None

        dfs(result_mid)
        result_mid = result_mid_temp
        fish_info = fish_info_temp
        fish_map = fish_map_temp
        shark = shark_temp

    if result_mid > result:
        result = result_mid

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
    'direction': fish_info[(0, 0)]['direction']
}

fish_map.pop(fish_info[(0, 0)]['number'])
fish_info[(0, 0)] = None

result = 0
dfs(0)
print(result)
