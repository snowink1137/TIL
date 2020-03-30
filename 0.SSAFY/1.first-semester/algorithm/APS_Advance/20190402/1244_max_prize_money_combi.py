import sys
from itertools import combinations

sys.stdin = open('1244.txt', 'r')


def check(original_numbers, k):
    global result
    global flag

    if flag:
        return

    if k == times:
        for i in range(l-1):
            if original_numbers[i] < original_numbers[i+1]:
                break
        else:
            flag = True

        number = int(''.join(original_numbers))
        result = max(result, number)
        return

    for combination in combinations(range(l), 2):
        if flag:
            return

        numbers = original_numbers[:]
        numbers[combination[0]], numbers[combination[1]] = numbers[combination[1]], numbers[combination[0]]
        if numbers not in storage[k]:
            storage[k].append(numbers)
            check(numbers, k+1)

        if flag:
            return


T = int(input())
for test_case in range(1, T+1):
    numbers, times = map(int, input().split())
    numbers = list(str(numbers))
    l = len(numbers)

    # combi = []
    # for i in range(l):
    #     for j in range(i+1, l):
    #         combi.append((i, j))

    storage = [[] for _ in range(times)]
    result = 0
    flag = False
    check(numbers, 0)
    print('#{} {}'.format(test_case, result))
