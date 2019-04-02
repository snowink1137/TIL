import sys

sys.stdin = open('1952.txt', 'r')


def dfs(k, acc):
    global result

    if k > 11:
        result = min(result, acc)
        return

    if acc >= result:
        return

    for i in range(k, 12):
        if month_plans[i] == 0:
            continue

        dfs(i+1, acc+prices[0]*month_plans[i])
        dfs(i+1, acc+prices[1])
        dfs(i+3, acc+prices[2])
        break
    else:
        result = min(result, acc)


for test_case in range(1, int(input())+1):
    prices = list(map(int, input().split()))
    month_plans = list(map(int, input().split()))

    result = prices[3]
    dfs(0, 0)

    print('#{} {}'.format(test_case, result))
