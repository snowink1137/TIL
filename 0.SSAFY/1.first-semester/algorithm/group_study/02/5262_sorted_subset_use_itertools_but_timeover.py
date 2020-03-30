import sys
import itertools

sys.stdin = open('5262_sample_input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    information = list(map(int, input().split()))

    N = information[0]
    numbers = information[1:]

    result = 1
    flag = False
    for k in range(N, 1, -1):
        combinations = itertools.combinations(range(N), k)
        for combi in combinations:
            for m in range(k-1):
                if numbers[combi[m]] < numbers[combi[m+1]]:
                    continue
                else:
                    break
            else:
                result = k
                flag = True
                break

        if flag:
            break

    print('#{} {}'.format(test_case, result))
