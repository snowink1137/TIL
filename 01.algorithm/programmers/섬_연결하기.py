def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    for cost in costs:
        if parent[cost[0]] == parent[cost[1]]:
            continue

        union_parent(parent, cost[0], cost[1])

        answer += cost[2]

    return answer


def find_parent(parent, target):
    if parent[target] == target:
        return target

    return find_parent(parent, parent[target])


def union_parent(parent, target1, target2):
    parent1 = find_parent(parent, target1)
    parent2 = find_parent(parent, target2)

    if (parent1 < parent2):
        parent[target2] = parent1
    else:
        parent[target1] = parent2


n = 6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
print(solution(n, costs))
