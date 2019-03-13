import sys

sys.stdin = open('2775.txt', 'r')


def check(k, n):
    if k == 0:
        return n

    result = 0
    for i in range(1, n+1):
        result += check(k-1, i)

    return result


T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    n = int(input())

    people = check(k, n)
    print(people)
