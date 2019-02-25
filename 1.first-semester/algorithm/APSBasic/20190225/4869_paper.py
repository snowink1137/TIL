import sys

sys.stdin = open('4869_sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    twenty = N // 20

    result = 0
    for i in range(twenty+1):
        j = (N - 20 * i) // 10
        length = i + j

        combination = 1
        div_factor = 1
        for k in range(0, i):
            combination *= length - k
            div_factor *= i - k

        result += 2 ** i * (combination / div_factor)

    print(f'#{test_case} {int(result)}')
