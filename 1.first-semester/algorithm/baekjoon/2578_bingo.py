import sys

sys.stdin = open('2578.txt', 'r')


def check():
    cnt = 0
    for i in range(5):
        if sum(bingo[i]) == 0:
            cnt += 1

    for j in range(5):
        temp_sum = 0
        for i in range(5):
            temp_sum += bingo[i][j]
            if temp_sum != 0:
                break
        else:
            cnt += 1

    temp_sum = 0
    for i in range(5):
        temp_sum += bingo[i][j]
        if temp_sum != 0:
            break
    else:
        cnt += 1

    temp_sum = 0
    for i in range(5):
        temp_sum += bingo[0+i][4-i]
        if temp_sum != 0:
            break
    else:
        cnt += 1

    return cnt


def search_and_delete(number):
    for i in range(5):
        if number in bingo[i]:
            j = bingo[i].index(number)
            bingo[i][j] = 0


bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

call_order = []
for _ in range(5):
    call_order.extend(map(int, input().split()))

flag = False
while True:
    for i in range(25):
        stage = call_order[i]
        search_and_delete(stage)
        bingo_num = check()
        if bingo_num > 2:
            result = i + 1
            flag = True
            break

    if flag:
        break

print(result)
