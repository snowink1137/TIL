import sys
from itertools import combinations, product

sys.stdin = open('2112.txt', 'r')


def check(film, cnt):
    if cnt == 0:
        test_film = [film[i][:] for i in range(D)]
        for j in range(W):
            acc = 0
            for i in range(D-1):
                if acc == K-1:
                    break

                if test_film[i][j] == test_film[i+1][j]:
                    acc += 1
                else:
                    acc = 0

            if acc != K-1:
                return False

        return True

    for combination in combinations(range(D), cnt):
        for prod in product(range(2), repeat=cnt):
            test_film = [film[i][:] for i in range(D)]
            flag = False
            for i in combination:
                test_film[i] = [prod[i]] * W

            for j in range(W):
                acc = 0
                for i in range(D - 1):
                    if acc == K - 1:
                        break

                    if test_film[i][j] == test_film[i + 1][j]:
                        acc += 1
                    else:
                        acc = 0

                if acc != K - 1:
                    flag = True
                    break

            if flag:
                continue

            return True


T = int(input())
for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    cnt = 0
    result = check(film, cnt)
    if result:
        print('#{} {}'.format(test_case, cnt))
        continue

    cnt = 2
    while True:
        result = check(film, cnt)
        if result:
            break

        cnt += 1

    print('#{} {}'.format(test_case, cnt))
