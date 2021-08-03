import sys

sys.stdin = open('5188_sample_input.txt', 'r')


def dfs(start, end):
    global min_sum
    v = start
    visit[v] = True
    stack.append(v)

    if v == end:
        count = len(stack)
        temp = 0
        for i in range(count):
            temp += matrix[(stack[i]-1)//N][(stack[i]+N-1) % N]

        if temp < min_sum:
            min_sum = temp

        stack.pop()
        return

    for i in range(node):
        if graph[v][i] == 1 and not visit[i]:
            dfs(i, end)
            visit[i] = False

    stack.pop()


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    last = N * (N-1)
    node = N * N + 1

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    graph = [[0]*node for _ in range(node)]
    for i in range(1, N*N):
        if i % N != 0 and i <= last:
            graph[i][i+1] = 1
            graph[i][i+N] = 1
        elif i % N == 0:
            graph[i][i+N] = 1
        elif i > last:
            graph[i][i+1] = 1

    visit = [False for _ in range(node)]
    stack = []
    min_sum = (N-1) * 2 * 13
    dfs(1, N*N)
    print(f'#{test_case} {min_sum}')
