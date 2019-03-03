import sys

sys.stdin = open('5204_sample_input.txt', 'r')


def count(m):
    global cnt
    if len(m) <= 1:
            return

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    if max(left) > max(right):
        cnt += 1

    count(left)
    count(right)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    m = list(map(int, input().split()))
    cnt = 0
    count(m)
    m.sort()

    print(f'#{test_case} {m[N//2]} {cnt}')
