def solution(grid):
    answer = []
    size_x = len(grid)
    size_y = len(grid[0])

    grid_map = [['W' for _ in range(size_y + 2)]]
    for g in grid:
        grid_map.append(['W'] + list(g) + ['W'])

    grid_map.append(['W' for _ in range(size_y + 2)])

    global_visit = {}
    for i in range(1, size_x+1):
        for j in range(1, size_y+1):
            for d in ['right', 'down', 'left', 'up']:
                if global_visit.get((i, j, d)):
                    continue

                location = (i, j, d)
                visit = []
                first = True

                while first or (visit[0] != location):
                    if global_visit.get(location):
                        break

                    visit.append(location)
                    x = location[0]
                    y = location[1]
                    d = location[2]

                    if d == 'right':
                        new_x = x
                        new_y = y + 1
                        new_d = d

                        if grid_map[new_x][new_y] == 'W':
                            new_y = 1

                        path = grid_map[new_x][new_y]

                        if path == 'L':
                            new_d = 'up'
                        elif path == 'R':
                            new_d = 'down'
                    elif d == 'down':
                        new_x = x + 1
                        new_y = y
                        new_d = d

                        if grid_map[new_x][new_y] == 'W':
                            new_x = 1

                        path = grid_map[new_x][new_y]

                        if path == 'L':
                            new_d = 'right'
                        elif path == 'R':
                            new_d = 'left'
                    elif d == 'left':
                        new_x = x
                        new_y = y - 1
                        new_d = d

                        if grid_map[new_x][new_y] == 'W':
                            new_y = size_y

                        path = grid_map[new_x][new_y]

                        if path == 'L':
                            new_d = 'down'
                        elif path == 'R':
                            new_d = 'up'
                    elif d == 'up':
                        new_x = x - 1
                        new_y = y
                        new_d = d

                        if grid_map[new_x][new_y] == 'W':
                            new_x = size_x

                        path = grid_map[new_x][new_y]

                        if path == 'L':
                            new_d = 'left'
                        elif path == 'R':
                            new_d = 'right'

                    location = (new_x, new_y, new_d)
                    first = False

                if visit[0] == location:
                    for l in visit:
                        global_visit[l] = True

                answer.append(len(visit))

    answer.sort()

    return answer


grid = ["S"]
print(solution(grid))
