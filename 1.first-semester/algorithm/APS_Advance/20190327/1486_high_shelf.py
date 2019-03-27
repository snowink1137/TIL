import sys
from itertools import combinations

sys.stdin = open('1486.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    min_difference = (N+1) * 10000
    for k in range(1, N+1):
        for i in combinations(heights, k):
            temp = 0
            for j in range(len(i)):
                temp += i[j]

            temp_difference = temp - B
            if 0 <= temp_difference < min_difference:
                min_difference = temp_difference

    print('#{} {}'.format(test_case, min_difference))
