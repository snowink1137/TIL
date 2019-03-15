import sys

sys.stdin = open('2007.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    string = input()

    result = 30
    for k in range(1, 30):
        flag = False
        for i in range(30-k):
            if string[i] == string[i+k]:
                continue
            else:
                break
        else:
            flag = True
            repeat = k

        if flag:
            result = repeat
            break

    print('#{} {}'.format(test_case, result))
