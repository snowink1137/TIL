import sys

sys.stdin = open('4843_sample_input.txt')
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    length = len(numbers)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    mid = int(N/2)
    odd_numbers = numbers[:mid]
    even_numbers = numbers[mid:]

    result = [0] * N
    flag = 1
    for i in range(mid):
        result[2*i] = even_numbers[mid-1-i]
        result[2*i + 1] = odd_numbers[i]

    print(f'#{test_case}', end='')
    for i in range(10):
        print(f' {result[i]}', end='')

    print()
