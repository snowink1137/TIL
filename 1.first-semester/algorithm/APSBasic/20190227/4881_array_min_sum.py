import sys

sys.stdin = open('4881_sample_input.txt', 'r')


def perm(k, n, visit,sum_what=0): # k: 시작 상태, n: 단말 노드의 높이
    global min_sum
    if k == n:
        sum = 0
        for index, ord in enumerate(order):
            sum += matrix[index][ord]

        if sum < min_sum:
            min_sum = sum


    for i in range(n):
        if visit & (1 << i):
            continue
        if sum_what < min_sum:
            order[k] = i
            perm(k+1, n, visit | (1 << i),sum_what+matrix[k][i])


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    order = [0] * N
    min_sum = 10*N*N

    perm(0, N, 0)
    # min_sum = 10 * N * N

    # for perm_element in perm_list:
    #     temp = 0
    #     for j in range(N):
    #         temp += matrix[j][perm_element[j]]
    #     if temp < min_sum:
    #         min_sum = temp

    print(f'#{test_case} {min_sum}')
