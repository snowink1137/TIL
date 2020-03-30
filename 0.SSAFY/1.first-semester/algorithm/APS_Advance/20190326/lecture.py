# # 1. knapsack 문제(memo x)
# w = [0, 5, 4, 6, 3]
# v = [0, 10, 40, 30, 50]
# N = len(v) - 1
# maxW, maxV = 10, 0
#
#
# def knapsack(k, W):
#     global maxV
#     if k == 0 or W == 0:
#         return 0
#
#     case1 = case2 = 0
#     if W >= w[k]:
#         case1 = knapsack(k-1, W-w[k]) + v[k]
#
#     case2 = knapsack(k-1, W)
#
#     return case1 if case1 > case2 else case2
#
#
# print(knapsack(N, maxW))


# 2. knapsack 문제(memo)
w = [0, 5, 4, 6, 3]
v = [0, 10, 40, 30, 50]
N = len(v) - 1
maxW, maxV = 10, 0


def knapsack(k, W):
    global maxV
    if k == 0 or W == 0:
        return 0

    if memo[k][W] != -1:
        return memo[k][W]

    case1 = case2 = 0
    if W >= w[k]:
        case1 = knapsack(k-1, W-w[k]) + v[k]

    case2 = knapsack(k-1, W)
    memo[k][W] = case1 if case1 > case2 else case2

    return memo[k][W]


memo = [[-1] * (maxW + 1) for _ in range(N + 1)]

for i in range(N + 1):
    memo[i][0] = 0
for i in range(maxW + 1):
    memo[0][i] = 0

print('최대가치 = %d' % (knapsack(N, maxW)))

print('----------------------------------')
for i in range(1, N + 1):
    for j in range(1, maxW + 1):
        print('%2d' % memo[i][j], end=' ')
    print()
