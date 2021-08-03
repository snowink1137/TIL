def dfs(v, first=False, second=False):
    if first:
        print('[{}]'.format(v), end='')
        cnt = 0
        for vv in G[v]:
            if cnt == 0:
                print('--+--', end='')
                dfs(vv, second=True)
            else:
                print()
                print('      +--', end='')
                dfs(vv, second=True)
            cnt += 1
    elif second:
        print('[{}]'.format(v), end='')
        for vv in G[v]:
            dfs(vv)
    else:
        print('-----[{}]'.format(v), end='')
        for vv in G[v]:
            dfs(vv)


G = [[] for _ in range(1000)]

G[30] = [54, 2, 45]
G[54] = [1]
G[45] = [123]

dfs(30, first=True)