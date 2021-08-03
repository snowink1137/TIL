# 자료: 상어 위치 및 냄새 지도, 상어 이동 정보, 상어 상태 및 위치 정보, 냄새 상태 및 위치 정보
# 기능: 상어 이동 및 삭제 처리, 남은 상어 판단, 냄새 만들고 없애기
import sys

sys.stdin = open('19237_sample_input.txt', 'r')


def move(shark_number):
    location = sharks_info[i]['location']
    direction = sharks_info[i]['direction']
    new_location = None

    possible_location = []
    for next_direction in sharks_info[i]['direction_rule'][direction]:
        if next_direction == 1:
            new_x, new_y = location[0] - 1, location[1]

            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            if not smell_map.get((new_x, new_y)):
                new_location = (new_x, new_y)
                sharks_info[i]['direction'] = next_direction
                return new_location

            if smell_map.get((new_x, new_y))[0] == shark_number:
                possible_location.append((new_x, new_y, next_direction))
        elif next_direction == 2:
            new_x, new_y = location[0] + 1, location[1]

            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            if not smell_map.get((new_x, new_y)):
                new_location = (new_x, new_y)
                sharks_info[i]['direction'] = next_direction
                return new_location

            if smell_map.get((new_x, new_y))[0] == shark_number:
                possible_location.append((new_x, new_y, next_direction))
        elif next_direction == 3:
            new_x, new_y = location[0], location[1] - 1

            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            if not smell_map.get((new_x, new_y)):
                new_location = (new_x, new_y)
                sharks_info[i]['direction'] = next_direction
                return new_location

            if smell_map.get((new_x, new_y))[0] == shark_number:
                possible_location.append((new_x, new_y, next_direction))
        elif next_direction == 4:
            new_x, new_y = location[0], location[1] + 1

            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            if not smell_map.get((new_x, new_y)):
                new_location = (new_x, new_y)
                sharks_info[i]['direction'] = next_direction
                return new_location

            if smell_map.get((new_x, new_y))[0] == shark_number:
                possible_location.append((new_x, new_y, next_direction))

    if possible_location:
        sharks_info[i]['direction'] = possible_location[0][2]
        return possible_location[0][0], possible_location[0][1]
    else:
        return location


N, M, k = map(int, input().split())

sea_map = [list(map(int, input().split())) for _ in range(N)]
sharks_info = {}
for i in range(N):
    for j in range(N):
        if sea_map[i][j]:
            sharks_info[sea_map[i][j]] = {
                'location': (i, j),
                'direction': 0,
                'direction_rule': {},
            }

initial_direction = list(map(int, input().split()))
for i in range(1, len(initial_direction)+1):
    sharks_info[i]['direction'] = initial_direction[i-1]

for i in range(1, M+1):
    for j in range(1, 5):
        sharks_info[i]['direction_rule'][j] = tuple(map(int, input().split()))

result = -1
cnt = 1
smell_map = {}
while cnt <= 1000:
    sharks_map = {}
    for i in sharks_info.keys():
        smell_map[sharks_info[i]['location']] = [i, k]

    for i in list(sharks_info.keys()):
        new_location = move(i)

        if sharks_map.get(new_location):
            before_shark_number = sharks_map.get(new_location)
            if i < before_shark_number:
                sharks_map[new_location] = i
                sharks_info.pop(before_shark_number)
                sharks_info[i]['location'] = new_location
            else:
                sharks_info.pop(i)
        else:
            sharks_map[new_location] = i
            sharks_info[i]['location'] = new_location

    for smell_location in list(smell_map.keys()):
        smell_map[smell_location][1] -= 1
        if smell_map[smell_location][1] == 0:
            smell_map.pop(smell_location)

    if len(sharks_info) == 1:
        result = cnt
        break

    cnt += 1

print(result)
