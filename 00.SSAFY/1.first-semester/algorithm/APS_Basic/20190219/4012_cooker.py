import sys

sys.stdin = open('4012_sample_input.txt', 'r')
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ingredients = [x for x in range(N)]

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    combinations = []
    rule = N/2
    for i in range(1 << N):
        cnt = 0
        temp = []
        for j in range(N):
            if cnt > rule:
                break

            if i & (1 << j):
                cnt += 1
                temp.append(ingredients[N-1-j])
        else:
            if cnt == rule:
                combinations.append(temp)

    min_gap = 19999 * rule
    for combination in combinations:
        another_combination = ingredients[:]
        combination_sum = 0
        for element_i in combination:
            another_combination.remove(element_i)
            for element_j in combination:
                if element_i == element_j:
                    continue
                combination_sum += matrix[element_i][element_j]

        another_sum = 0
        for element_i in another_combination:
            for element_j in another_combination:
                if element_i == element_j:
                    continue
                another_sum += matrix[element_i][element_j]

        gap = abs(combination_sum - another_sum)
        if gap < min_gap:
            min_gap = gap

    print(f'#{test_case} {min_gap}')

