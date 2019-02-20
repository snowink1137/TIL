import sys

convert_num = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9
}
convert_str = {
    0: 'ZRO',
    1: 'ONE',
    2: 'TWO',
    3: 'THR',
    4: 'FOR',
    5: 'FIV',
    6: 'SIX',
    7: 'SVN',
    8: 'EGT',
    9: 'NIN'
}


def to_number(num_str):
    return convert_num[num_str]


def to_str(num):
    return convert_str[num]


sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    C, N = tuple(input().split())
    N = int(N)

    numbers = list(map(to_number, input().split()))
    count_list = [0] * 10
    for elem in numbers:
        count_list[elem] += 1

    numbers = []
    for idx in convert_str.keys():
        numbers += [convert_str[idx]] * count_list[idx]

    print(C)
    print(' '.join(numbers))
