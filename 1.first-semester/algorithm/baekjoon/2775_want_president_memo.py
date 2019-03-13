import sys

sys.stdin = open('2775.txt', 'r')


def check(k, n):
    if k == 0:
        if memo[k][n]:
            return memo[k][n]

        memo[k][n] = n
        return n

    result = 0
    for i in range(1, n+1):
        if memo[k-1][i]:
            result += memo[k-1][i]
        else:
            result += check(k-1, i)
            memo[k-1][i] = check(k-1, i)

    memo[k][n] = result
    return result


T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    n = int(input())

    memo = [[0] * (n+1) for _ in range(k+1)]
    people = check(k, n)
    print(people)
