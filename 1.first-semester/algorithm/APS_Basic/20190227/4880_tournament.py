import sys

sys.stdin = open('4880_sample_input.txt', 'r')


def get_max(low, high):
    if low == high:
        return information[low], low
    mid = (low + high) >> 1
    l, l_index = get_max(low, mid)
    r, r_index = get_max(mid+1, high)

    if r == 3 and l == 2:
        out = r, r_index
    elif r == 2 and l == 1:
        out = r, r_index
    elif r == 1 and l == 3:
        out = r, r_index
    else:
        out = l, l_index

    return out


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    information = list(map(int, input().split()))

    result, result_index = get_max(0, N-1)
    print(f'#{test_case} {result_index+1}')

