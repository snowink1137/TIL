import sys

sys.stdin = open('17143_sample_input.txt', 'r')

result = 0

R, C, M = map(int, input().split())
sharks = [False for _ in range(M)]
for i in range(M):
    sharks[i] = list(map(int, input().split()))
    sharks[i][0] -= 1
    sharks[i][1] -= 1

sharks_map = [[False for _ in range(C)] for _ in range(R)]
for i in range(len(sharks)):
    sharks_map[sharks[i][0]][sharks[i][1]] = i

for j in range(C):
    # 낚시
    for i in range(R):
        if type(sharks_map[i][j]) == int:
            result += sharks[sharks_map[i][j]][4]
            sharks[sharks_map[i][j]] = False
            sharks_map[i][j] = False
            break

    # 상어 움직이기
    for i in range(len(sharks)):
        if not sharks[i]:
            continue

        r, c, s, d = sharks[i][0], sharks[i][1], sharks[i][2], sharks[i][3]
        if 1 <= d <= 2:
            if d == 1:
                step = -1
            else:
                step = 1

            new_r = r
            while s:
                new_r += step
                if new_r < 0 or new_r >= R:
                    step *= -1
                    new_r += 2 * step
                    if step == -1:
                        d = 1
                    else:
                        d = 2

                s -= 1

            sharks[i][0] = new_r
            sharks[i][3] = d
        else:
            if d == 3:
                step = 1
            else:
                step = -1

            new_c = c
            while s:
                new_c += step
                if new_c < 0 or new_c >= C:
                    step *= -1
                    new_c += 2 * step
                    if step == -1:
                        d = 4
                    else:
                        d = 3

                s -= 1

            sharks[i][1] = new_c
            sharks[i][3] = d

    # 상어 지도 업데이트
    sharks_map = [[False for _ in range(C)] for _ in range(R)]
    for i in range(len(sharks)):
        if not sharks[i]:
            continue

        if type(sharks_map[sharks[i][0]][sharks[i][1]]) == int:
            compare_shark_idx = sharks_map[sharks[i][0]][sharks[i][1]]
            if sharks[compare_shark_idx][4] < sharks[i][4]:
                sharks[compare_shark_idx] = False
                sharks_map[sharks[i][0]][sharks[i][1]] = i
            else:
                sharks[i] = False
        else:
            sharks_map[sharks[i][0]][sharks[i][1]] = i

print(result)
