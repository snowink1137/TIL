import sys

sys.stdin = open('4865_sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    p = input()
    t = input()

    max = 0
    for i in p:
        temp = 0
        for j in t:
            if i == j:
                temp += 1

        if temp > max:
            max = temp

    print(f'#{test_case} {max}')
