def solution(m, n, puddles):
    visit = [[1 for _ in range(m)] for _ in range(n)]

    for puddle in puddles:
        visit[puddle[1]-1][puddle[0]-1] = False

    for i in range(1, n):
        for j in range(1, m):
            new_i = i - 1
            new_j = j - 1

            if visit[i][j] == False:
                continue

            if visit[new_i][j] == False and visit[i][new_j] == False:
                visit[i][j] = False
            elif visit[new_i][j] == False:
                visit[i][j] = visit[i][new_j]
            elif visit[i][new_j] == False:
                visit[i][j] = visit[new_i][j]
            else:
                visit[i][j] = visit[new_i][j] + visit[i][new_j]

    return visit[n-1][m-1]


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
