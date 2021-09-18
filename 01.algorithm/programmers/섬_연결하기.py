def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    for cost in costs:
        parent1 = find_parent(parent, cost[0])
        parent2 = find_parent(parent, cost[1])
        if parent1 == parent2:
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

    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2


n = 5
costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]
print(solution(n, costs))
