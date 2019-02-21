import sys

sys.stdin = open('5185_sample_input.txt')

# def to_2_from_16(num):
#     three = num // 2
#     remain =

T = int(input())
for test_case in range(1, T+1):
    N, numbers = input().split()

    for number in numbers:
        num = int(number)

