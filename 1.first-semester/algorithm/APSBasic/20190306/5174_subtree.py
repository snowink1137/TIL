import sys

sys.stdin = open('5174_sample_input.txt', 'r')


def check_tree_size(v):
    global cnt
    if v == 0:
        return

    cnt += 1
    check_tree_size(L[v])
    check_tree_size(R[v])


T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    P = [0] * (E + 2)
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    target_node = []
    for i in range(len(arr)//2):
        u = 2 * i
        v = 2 * i + 1
        P[arr[v]] = arr[u]

        if arr[u] == N:
            target_node.append(arr[2*i])

        if L[arr[u]] == 0:
            L[arr[u]] = arr[v]
        else:
            R[arr[u]] = arr[v]

    if target_node:
        cnt_list = []
        for node in target_node:
            cnt = 0
            check_tree_size(node)
            cnt_list.append(cnt)

        result = max(cnt_list)
    else:
        result = N

    print('#{} {}'.format(test_case, result))
