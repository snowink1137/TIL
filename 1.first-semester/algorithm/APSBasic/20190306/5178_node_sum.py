import sys

sys.stdin = open('5178_sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(N-M, 0, -1):
        if 2*i+1 <= N:
            tree[i] = tree[2*i] + tree[2*i+1]
        else:
            tree[i] = tree[2*i]

    print('#{} {}'.format(test_case, tree[L]))
