from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10000000)
answer = 0


def dfs(node, visit, info_dict, nodes):
    global answer

    weight = nodes[node]
    visit[node] = True

    for i in info_dict[node]:
        if not visit[i]:
            weight += dfs(i, visit, info_dict, nodes)

    answer += abs(weight)
    return weight


def solution(a, edges):
    global answer

    if sum(a):
        return -1

    info_dict = defaultdict(list)
    for edge in edges:
        info_dict[edge[0]].append(edge[1])
        info_dict[edge[1]].append(edge[0])

    visit = [False for _ in range(len(a))]
    dfs(0, visit, info_dict, a)

    return answer


a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))
