from collections import defaultdict, deque


def bfs(start, graph, visit):
    queue = deque()
    queue.append(start)
    visit[start] = 1

    while queue:
        q = queue.pop()
        depth = visit[q]

        for g in graph[q]:
            if visit[g] <= depth + 1 and visit[g] != 0:
                continue

            queue.append(g)
            visit[g] = depth + 1

    max_depth = max(visit)
    count = visit.count(max_depth)

    return count


def solution(n, edge):
    answer = 0

    graph = defaultdict(list)
    for e in edge:
        n1 = e[0]
        n2 = e[1]

        graph[n1].append(n2)
        graph[n2].append(n1)

    visit = [0 for _ in range(n+1)]
    answer = bfs(1, graph, visit)
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
