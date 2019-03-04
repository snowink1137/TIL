import sys
import itertools

sys.stdin = open('5262_sample_input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    information = list(map(int, input().split()))

    N = information[0]
    numbers = information[1:]

    start1 = numbers[0]
    start1_temp = numbers[0]
    start1_cnt = 0
    start2 = 1001
    start2_temp = 1001
    start2_cnt = 0
    for number in numbers[1:]:
        if start1_temp < number:
            start1_cnt += 1

        if start2_temp < number:
            start2_cnt += 1

        if start1 > number:
            start2 = number

        if





    print('#{} {}'.format(test_case, result))
