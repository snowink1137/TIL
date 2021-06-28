def solution(m, n, puddles):
    visit = [[0 for _ in range(m)] for _ in range(n)]

    for puddle in puddles:
        visit[puddle[1]-1][puddle[0]-1] = 'water'

    for i in range(n):
        if visit[i][0] == 'water':
            break

        visit[i][0] = 1

    for j in range(m):
        if visit[0][j] == 'water':
            break

        visit[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            new_i = i - 1
            new_j = j - 1

            if visit[i][j] == 'water':
                continue

            if visit[new_i][j] == 'water' and visit[i][new_j] == 'water':
                visit[i][j] = 'water'
            elif visit[new_i][j] == 'water':
                visit[i][j] = visit[i][new_j]
            elif visit[i][new_j] == 'water':
                visit[i][j] = visit[new_i][j]
            else:
                visit[i][j] = visit[new_i][j] + visit[i][new_j]

    return visit[n-1][m-1] % 1000000007


m = 4
n = 3
puddles = [[2, 2]]
# puddles = [[1,3],[3,1]]
print(solution(m, n, puddles))
