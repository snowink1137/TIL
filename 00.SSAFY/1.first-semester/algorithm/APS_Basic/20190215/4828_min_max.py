import sys


sys.stdin = open('4828_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    length = int(input())

    num_list = list(map(int, input().split()))

    if num_list[0] < num_list[1]:
        max_value = num_list[1]
        min_value = num_list[0]
    else:
        max_value = num_list[0]
        min_value = num_list[1]

    for num in num_list[2:]:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    result = max_value - min_value
    print(f'#{test_case} {result}')
