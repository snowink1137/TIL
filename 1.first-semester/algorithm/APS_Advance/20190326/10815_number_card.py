import sys

sys.stdin = open('10815.txt', 'r')


def search(num, l, r):
    if abs(l - r) == 1:
        if numbers[l] == num or numbers[r] == num:
            result.append(1)
            return
        else:
            result.append(0)
            return

    m = (l+r) // 2

    if num > numbers[m]:
        search(num, m, r)
    else:
        search(num, l, m)


N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
guess_numbers = list(map(int, input().split()))

numbers.sort()
result = []
for num in guess_numbers:
    search(num, 0, N-1)

print(' '.join(map(str, result)))
