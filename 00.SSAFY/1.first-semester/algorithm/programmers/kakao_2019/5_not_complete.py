def solution(n, build_frame):
    check = [[[[] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    answer = []

    for build in build_frame:
        x = build[0]
        y = build[1]
        type = build[2]
        act = build[3]

        if act == 1:
            if type == 0:
                if y == 0 or check[x][y]:
                    check[x][y].append(0)
                    check[x][y+1].append(0)
                    answer.append([x, y, 0])
            else:
                if y == 0 or check
        else:
            if build[2] == 0:
                pass
            else:
                pass

    return answer


solution(3, [])