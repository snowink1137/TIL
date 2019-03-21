import sys

sys.stdin = open('4839_sample_input.txt')
T = int(input())

for test_case in range(1, T + 1):
    information = list(map(int, input().split()))
    total = information[0]
    a = information[1]
    a_start = 1
    a_end = total
    b = information[2]
    b_start = 1
    b_end = total

    a_win = False
    b_win = False
    while True:
        a_mid = int((a_start+a_end)/2)
        b_mid = int((b_start+b_end)/2)

        if a > a_mid:
            a_start = a_mid
        elif a < a_mid:
            a_end = a_mid
        else:
            a_win = True

        if b > b_mid:
            b_start = b_mid
        elif b < b_mid:
            b_end = b_mid
        else:
            b_win = True

        if a_win and b_win:
            result = 0
            break
        elif a_win:
            result = 'A'
            break
        elif b_win:
            result = 'B'
            break

    print(f'#{test_case} {result}')
