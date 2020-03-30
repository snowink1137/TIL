import sys

sys.stdin = open('4871_sample_input.txt', 'r')


def dfs(start, end):
    global result
    v = start
    visit[v] = True
    stack.append(v)

    if v == end:
        result = 1
        return

    for i in range(1, V+1):
        if information[v][i] == 1 and not visit[i]:
            dfs(i, end)

    stack.pop()


T = int(input())
for test_case in range(1, T+1):
    V, E = tuple(map(int, input().split()))

    information = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = tuple(map(int, input().split()))
        information[i][j] = 1

    S, G = tuple(map(int, input().split()))

    visit = [False for _ in range(V+1)]
    stack = []
    result = 0
    dfs(S, G)

    print(f'#{test_case} {result}')
