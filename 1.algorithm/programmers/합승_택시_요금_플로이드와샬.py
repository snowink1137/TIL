def solution(n, s, a, b, fares):
    INF = 1e9
    answer = INF

    graph_list = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for fare in fares:
        graph_list[fare[0]][fare[1]] = fare[2]
        graph_list[fare[1]][fare[0]] = fare[2]

    for i in range(n+1):
        graph_list[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if graph_list[i][j] > graph_list[i][k] + graph_list[k][j]:
                    graph_list[i][j] = graph_list[i][k] + graph_list[k][j]
                    graph_list[j][i] = graph_list[i][k] + graph_list[k][j]

    for k in range(1, n+1):
        if answer > graph_list[s][k] + graph_list[k][a] + graph_list[k][b]:
            answer = graph_list[s][k] + graph_list[k][a] + graph_list[k][b]

    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))
