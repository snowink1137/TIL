import sys

sys.stdin = open('17825_sample_input.txt', 'r')

grid_dict = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [21, 22, 23, 24, 25],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [27, 28, 24, 25, 26],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [29, 30, 31, 24, 25],
    16: [17, 18, 19, 20, -1],
    17: [18, 19, 20, -1, -1],
    18: [19, 20, -1, -1, -1],
    19: [20, -1, -1, -1, -1],
    20: [-1, -1, -1, -1, -1],
    21: [22, 23, 24, 25, 26],
    22: [23, 24, 25, 26, 20],
    23: [24, 25, 26, 20, -1],
    24: [25, 26, 20, -1, -1],
    25: [26, 20, -1, -1, -1],
    26: [20, -1, -1, -1, -1],
    27: [28, 24, 25, 26, 20],
    28: [24, 25, 26, 20, -1],
    29: [30, 31, 24, 25, 26],
    30: [31, 24, 25, 26, 20],
    31: [24, 25, 26, 20, -1]
}

score_dict = {
    -1: 0, 0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20,
    11: 22, 12: 24, 13: 26, 14: 28, 15: 30, 16: 32, 17: 34, 18: 36, 19: 38, 20: 40, 21: 13, 22: 16,
    23: 19, 24: 25, 25: 30, 26: 35, 27: 22, 28: 24, 29: 28, 30: 27, 31: 26
}


def dfs(cnt, total=0):
    global result

    if cnt == 10:
        if total > result:
            result = total

        return

    for i in range(4):
        horse_num = i
        dice = dices[cnt]
        location = horses[horse_num]
        if location == -1:
            continue

        next_location = grid_dict[location][dice-1]
        if next_location == -1:
            pass
        elif game_map[next_location]:
            continue

        temp = score_dict[next_location]

        game_map[next_location] = True
        game_map[location] = False
        horses[horse_num] = next_location
        dfs(cnt+1, total+temp)
        game_map[next_location] = False
        game_map[location] = True
        horses[horse_num] = location


result = 0
dices = list(map(int, input().split()))

game_map = [False for i in range(33)]
horses = [0, 0, 0, 0]

next_location = grid_dict[0][dices[0]-1]
game_map[next_location] = True
horses[0] = next_location

tot = score_dict[next_location]

dfs(1, tot)
print(result)
