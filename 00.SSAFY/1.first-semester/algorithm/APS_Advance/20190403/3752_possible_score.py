import sys

sys.stdin = open('3752.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = tuple(map(int, input().split()))
    max_score = sum(numbers)

    visit = [False for _ in range(max_score+1)]
    visit[0] = True

    result = 1
    max_score = 0
    for num in numbers:
        max_score += num
        for i in range(max_score, -1, -1):
            if visit[i]:
                visit[i+num] = True
                result += 1

    result = sum(visit)
    print('#{} {}'.format(test_case, result))
