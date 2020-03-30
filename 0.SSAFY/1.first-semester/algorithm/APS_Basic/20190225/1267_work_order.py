import sys

sys.stdin = open('1267_input.txt', 'r')


def dfs(start):
    for _ in range(len(children[start]) + 1):
        if _ == 0:
            visit[start] = True
            result.append(str(start))

        v = start
        stack = []
        stack.append(v)
        while len(stack) > 0:
            goback = True
            for child in children[v]:
                for p in parents[child]:
                    if not visit[p]:
                        break
                else:
                    if not visit[child]:
                        visit[child] = True
                        stack.append(v)
                        result.append(str(child))
                        v = child
                        goback = False
                        break

            if goback:
                v = stack.pop()


for test_case in range(1, 11):
    V, E = tuple(map(int, input().split()))

    edge = list(map(int, input().split()))
    parents = [[] for _ in range(V + 1)]
    children = [[] for _ in range(V + 1)]
    for i in range(E):
        parents[edge[2 * i + 1]].append(edge[2 * i])
        children[edge[2 * i]].append(edge[2 * i + 1])

    visit = [False for _ in range(V + 1)]
    result = []

    no_parent_node = []
    for i in range(1, V + 1):
        if len(parents[i]) == 0:
            no_parent_node.append(i)

    for i in no_parent_node:
        dfs(i)

    print(f'#{test_case} {" ".join(result)}')
