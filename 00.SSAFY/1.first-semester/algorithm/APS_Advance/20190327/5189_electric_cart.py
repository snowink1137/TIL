import sys
from itertools import permutations

sys.stdin = open('5189.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_result = N * N * 100
    for i in permutations([i for i in range(1, N)]):
        temp = matrix[0][i[0]] + matrix[i[-1]][0]
        for j in range(0, N-2):
            temp += matrix[i[j]][i[j+1]]

        if temp < min_result:
            min_result = temp

    print('#{} {}'.format(test_case, min_result))
