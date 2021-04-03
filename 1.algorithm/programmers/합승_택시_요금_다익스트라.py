import heapq as hq

INF = 1e9


def dijkstra(n, graph_matrix, start):
    global INF
    distance_list = [INF for _ in range(n+1)]
    distance_list[start] = 0

    pq = []
    hq.heappush(pq, [distance_list[start], start])
    while pq:
        distance, destination = hq.heappop(pq)
        if distance_list[destination] >= distance:
            for i in range(1, n+1):
                new_distance = distance + graph_matrix[destination][i]

                if new_distance < distance_list[i]:
                    distance_list[i] = new_distance
                    hq.heappush(pq, [new_distance, i])

    return distance_list


def solution(n, s, a, b, fares):
    global INF
    answer = INF

    graph_matrix = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for fare in fares:
        graph_matrix[fare[0]][fare[1]] = fare[2]
        graph_matrix[fare[1]][fare[0]] = fare[2]

    for i in range(1, n+1):
        graph_matrix[i][i] = 0

    update_graph_matrix = [[INF for _ in range(n+1)]]
    for i in range(1, n+1):
        update_graph_matrix.append(dijkstra(n, graph_matrix, i))

    for k in range(1, n+1):
        answer = min(answer, update_graph_matrix[s][k] + update_graph_matrix[k][a] + update_graph_matrix[k][b])

    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
