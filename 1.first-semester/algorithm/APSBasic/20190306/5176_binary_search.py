import sys

sys.stdin = open('5176_sample_input.txt', 'r')


def line_up(v):
    if v == 0:
        return

    line_up(node_left[v])
    line.append(v)
    line_up(node_right[v])


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    node_parent = [i//2 for i in range(N+1)]

    cnt = 0
    while True:
        if N < 2 ** cnt:
            height = cnt
            break
        else:
            cnt += 1
            continue

    node_left = [0] * (N + 1)
    for i in range(1, 2**(height-1)):
        if 2 * i <= N:
            node_left[i] = 2 * i

    node_right = [0] * (N + 1)
    for i in range(1, 2**(height-1)):
        if 2 * i + 1 <= N:
            node_right[i] = 2 * i + 1

    line = []
    line_up(1)

    tree = [0] * (N + 1)
    cnt = 0
    for node in line:
        cnt += 1
        tree[node] = cnt

    print('#{} {} {}'.format(test_case, tree[1], tree[N//2]))


