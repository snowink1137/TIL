import sys

sys.stdin = open('5248.txt', 'r')


def dfs_G(v):
    if v == [] or complete[v]:
        return

    complete[v] = 1
    for new_v in G[v]:
        dfs_G(new_v)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))
    complete = [0] * (N + 1)
    G = [[] for _ in range(N + 1)]

    for i in range(M):
        G[numbers[2*i]].append(numbers[2*i+1])
        G[numbers[2*i+1]].append(numbers[2*i])

    cnt = 0
    for i in range(1, N+1):
        if complete[i]:
            continue

        dfs_G(i)
        cnt += 1

    print('#{} {}'.format(test_case, cnt))
