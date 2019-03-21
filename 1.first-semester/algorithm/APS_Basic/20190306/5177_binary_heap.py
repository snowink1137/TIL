import sys

sys.stdin = open('5177_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    line = [0]
    line.extend(arr)
    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        tree[i] = line[i]
        parent = i // 2
        k = i
        while True:
            if parent == 0:
                break

            if tree[k] < tree[parent]:
                tree[k], tree[parent] = tree[parent], tree[k]
                k = parent

            parent = parent // 2

    parent_sum = 0
    parent_node = N
    while True:
        parent_node = parent_node // 2
        if parent_node == 0:
            break

        parent_sum += tree[parent_node]

    print('#{} {}'.format(test_case, parent_sum))
    print(tree)
