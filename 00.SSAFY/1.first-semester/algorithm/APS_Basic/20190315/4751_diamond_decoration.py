import sys

sys.stdin = open('4751.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    string = input()

    length = len(string)

    print('..#' + '...#' * (length-1) + '..')
    print('.#' * (length*2) + '.')
    print('#', end='')
    temp = ''
    for i in range(length):
        temp += '.' + string[i] + '.#'

    print(temp)
    print('.#' * (length * 2) + '.')
    print('..#' + '...#' * (length - 1) + '..')
