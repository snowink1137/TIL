import sys

sys.stdin = open('4408.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 for _ in range(401)]

    for i in range(1, 400):
        cnt = 0
        for zone in matrix:
            left = min(zone)
            right = max(zone)
            if left % 2 == 0 and right % 2 == 0:
                if left - 0.6 < i + 0.5 < right:
                    cnt += 1
            elif left % 2 == 0 and right % 2 != 0:
                if left - 0.6 < i + 0.5 < right + 0.6:
                    cnt += 1
            elif left % 2 != 0 and right % 2 == 0:
                if left < i + 0.5 < right - 0.4:
                    cnt += 1
            else:
                if left < i + 0.5 < right + 0.6:
                    cnt += 1

        visit[i] += cnt

    result = max(visit)
    print('#{} {}'.format(test_case, result))
