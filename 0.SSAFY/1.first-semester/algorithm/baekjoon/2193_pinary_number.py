import sys

sys.stdin = open('2193.txt', 'r')

N = int(input())

arr = [0] * (N+1)

arr[1] = 1
if N != 1:
    arr[2] = 1
    for i in range(3, N+1):
        arr[i] = arr[i-1] + arr[i-2]

print(arr[N])
