import sys

sys.stdin = open('5204_sample_input.txt', 'r')


def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global cnt
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    m = list(map(int, input().split()))
    cnt = 0
    output = merge_sort(m)[N//2]

    print(f'#{test_case} {output} {cnt}')
