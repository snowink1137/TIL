import sys

sys.stdin = open('10250.txt', 'r')

T = int(input())
for test_case in range(T):
    H, W, N = map(int, input().split())

    number = ((N-1) // H) + 1
    floor = N % H if N % H != 0 else H
    if number >= 10:
        result = str(floor)
        result += str(number)
    else:
        result = str(floor)
        result += '0' + str(number)

    print(result)
