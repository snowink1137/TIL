import sys

sys.stdin = open('4008.txt', 'r')


def check(depth, acc, plus, minus, multi, div):
    global max_result, min_result

    if depth == N-1:
        if acc > max_result:
            max_result = acc

        if acc < min_result:
            min_result = acc

        return

    for i in range(4):
        if i == 0:
            if plus > 0:
                check(depth+1, acc+numbers[depth+1], plus-1, minus, multi, div)
        elif i == 1:
            if minus > 0:
                check(depth + 1, acc-numbers[depth+1], plus, minus-1, multi, div)
        elif i == 2:
            if multi > 0:
                check(depth + 1, acc*numbers[depth+1], plus, minus, multi-1, div)
        elif i == 3:
            if div > 0:
                if acc < 0:
                    check(depth + 1, ((acc * -1) // numbers[depth+1]) * (-1), plus, minus, multi, div - 1)
                else:
                    check(depth + 1, acc//numbers[depth+1], plus, minus, multi, div - 1)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    plus, minus, multi, div = map(int, input().split())
    numbers = tuple(map(int, input().split()))

    min_result = 100000001
    max_result = -100000001
    check(0, numbers[0], plus, minus, multi, div)

    print('#{} {}'.format(test_case, max_result-min_result))
