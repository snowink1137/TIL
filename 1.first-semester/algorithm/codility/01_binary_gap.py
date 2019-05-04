def solution(N):
    result = 0
    limit = 0

    while True:
        if N > 2 ** limit:
            limit += 1
            continue

        break

    print(limit)
    flag = False
    where = 0
    for i in range(limit):
        if N & (1 << i):
            where = i
            flag = True
            break

    print('start', where)
    if flag:
        count = 0
        for i in range(where + 1, limit):
            if N & (1 << i):
                if count > result:
                    result = count

                count = 0
            else:
                count += 1

    return result


print(solution(561892))
