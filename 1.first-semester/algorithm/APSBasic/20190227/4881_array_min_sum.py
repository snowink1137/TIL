import sys

sys.stdin = open('4881_sample_input.txt', 'r')


def perm(k, n, visit, sum_what=0): # k: 시작 상태, n: 단말 노드의 높이
    global min_sum
    if k == n:
        if sum_what < min_sum:
            min_sum = sum_what

    for i in range(n):
        if visit & (1 << i):
            continue
        if sum_what < min_sum:
            order[k] = i
            perm(k+1, n, visit | (1 << i), sum_what+matrix[k][i])


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    order = [0] * N
    min_sum = 10 * N * N
    perm(0, N, 0)
    print(f'#{test_case} {min_sum}')
