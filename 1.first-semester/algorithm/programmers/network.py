def dfs(start, visit, computers):
    if visit[start]:
        return

    visit[start] = True

    for i in range(len(computers)):
        if computers[start][i]:
            dfs(i, visit, computers)


def solution(n, computers):
    answer = 0
    visit = [False for i in range(n)]

    for i in range(n):
        if visit[i]:
            continue
        else:
            dfs(i, visit, computers)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
