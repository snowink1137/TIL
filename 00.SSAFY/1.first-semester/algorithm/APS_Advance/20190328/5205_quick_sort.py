import sys

sys.stdin = open('5205.txt', 'r')


def partition(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1

        while arr[R] >= arr[pivot] and L < R:
            R -= 1

        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]

    arr[pivot], arr[R] = arr[R], arr[pivot]
    return R


def quick_sort(arr, begin, end):
    if begin < end:
        p = partition(arr, begin, end)
        quick_sort(arr, begin, p-1)
        quick_sort(arr, p+1, end)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr)-1)
    print('#{} {}'.format(test_case, arr[N//2]))
