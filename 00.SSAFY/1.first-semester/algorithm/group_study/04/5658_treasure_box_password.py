import sys

sys.stdin = open('5658.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    password_set = set()
    password = list(input())
    side = int(N / 4)
    for k in range(side):
        for i in range(4):
            temp = ''
            for j in range(side):
                temp += password[i*side + j]

            password_set.add(temp)

        password.append(password.pop(0))

    result_list = []
    for i in password_set:
        result_list.append(int(i, 16))

    result_list.sort(reverse=True)
    print('#{} {}'.format(test_case, result_list[K-1]))
