import sys
from itertools import permutations

sys.stdin = open('4008.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    plus, minus, multi, div = map(int, input().split())
    numbers = tuple(map(int, input().split()))

    iter = []
    if plus > 0:
        iter += [0] * plus
    if minus > 0:
        iter += [1] * minus
    if multi > 0:
        iter += [2] * multi
    if div > 0:
        iter += [3] * div

    perm_set = set(permutations(iter))

    min_result = 100000001
    max_result = -100000001
    for perm in perm_set:
        temp = numbers[0]
        for i in range(N-1):
            if perm[i] == 0:
                temp += numbers[i+1]
            elif perm[i] == 1:
                temp -= numbers[i+1]
            elif perm[i] == 2:
                temp *= numbers[i+1]
            elif perm[i] == 3:
                if temp < 0:
                    temp //= (-1) * numbers[i+1]
                    temp *= (-1)
                else:
                    temp //= numbers[i+1]

        if temp > max_result:
            max_result = temp
        elif temp < min_result:
            min_result = temp

    print('#{} {}'.format(test_case, max_result-min_result))
