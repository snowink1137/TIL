import sys

sys.stdin = open('2292.txt', 'r')

N = int(input())

cnt = 1
value = 1
while True:
    if N <= value:
        break
    else:
        cnt += 1
        value = 3 * (cnt ** 2) - (3 * cnt) + 1

print(cnt)
