import sys

sys.stdin = open('5120.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    sequence = list(map(int, input().split()))

    cur = M
    size = len(sequence)
    for _ in range(K):
        sequence.insert(cur, sequence[(cur-1) % size]+sequence[cur % size])
        size += 1
        cur = (cur + M) % size
        if cur == 0:
            cur = size

    result = reversed(sequence[-10:])
    print('#{} {}'.format(test_case, ' '.join(map(str, result))))
