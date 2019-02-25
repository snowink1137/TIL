import sys

sys.stdin = open('1267_input.txt', 'r')


def dfs(start):

    # for p in parents[v]:
    #     if not visit[p]:
    #         dfs(p)
    #         return

    # visit[v] = True
    # stack.append(v)
    # result.append(str(v))
    # count += 1

    # if count == V:
    #     return

    # for i in range(1, V+1):
    #     if information[v][i] and not visit[i]:
    #         dfs(i)
    # for child in children[v]:
    #     if not visit[child]:
    #         dfs(child)
    global count
    v = i
    visit[v] = True
    stack = []
    stack.append(v)
    result.append(str(v))
    count += 1
    children_length = len(children[start])
    child_sum = 0
    while len(stack) > 0 or (children_length > child_sum):
        goback = True
        flag = 0
        for child in children[v]:
            for p in parents[child]:
                if not visit[p]:
                    break
            else:
                if not visit[child]:
                    visit[child] = True
                    if flag == 1:
                        stack.append(v)

                    v = child
                    stack.append(v)
                    result.append(str(v))
                    count += 1
                    goback = False
                    break
            flag = 1

        if goback:
            if stack[-1] != start:
                v = stack.pop()
            else:
                v = start

        child_sum = 0
        for c in children[start]:
            child_sum += visit[c]


for test_case in range(1, 8):
    V, E = tuple(map(int, input().split()))

    information = [[False]*(V+1) for _ in range(V+1)]
    edge = list(map(int, input().split()))
    parents = [[] for _ in range(V+1)]
    children = [[] for _ in range(V+1)]
    for i in range(E):
        information[edge[2*i]][edge[2*i+1]] = True
        parents[edge[2*i+1]].append(edge[2*i])
        children[edge[2*i]].append(edge[2*i+1])

    visit = [False for _ in range(V+1)]
    result = []
    count = 0

    no_parent_node = []
    for i in range(1, V+1):
        if len(parents[i]) == 0:
            no_parent_node.append(i)

    for i in no_parent_node:
        dfs(i)

    print(f'#{test_case} {" ".join(result)}')

