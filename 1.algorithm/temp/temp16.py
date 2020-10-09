answer = 0
road_dict = dict()


def dfs(start, end, hub, flag=False):
    global answer
    if start == end:
        if flag:
            answer += 1

        return

    if road_dict.get(start):
        for go in road_dict[start]:
            if go == hub or flag:
                dfs(go, end, hub, True)
            else:
                dfs(go, end, hub)


def solution(depar, hub, dest, roads):
    global answer

    for road in roads:
        if road_dict.get(road[0]):
            road_dict[road[0]].append(road[1])
        else:
            road_dict[road[0]] = [road[1]]

    dfs(depar, dest, hub)

    return answer


depar = "ULSAN"
hub = "SEOUL"
dest = "BUSAN"
roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]
print(solution(depar, hub, dest, roads))
