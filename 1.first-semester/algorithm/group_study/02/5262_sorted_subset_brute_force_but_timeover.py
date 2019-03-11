import sys

sys.stdin = open('5262_sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    information = list(map(int, input().split()))
    result = 1
    for i in range(2 ** information[0]-1, 1, -1):
        flag = False
        cnt = 1
        memo = 0
        for j in range(information[0]):
            if i & (1 << j):
                if not flag:
                    flag = True
                    memo = information[0]-j
                else:
                    if information[information[0]-j] <= information[memo]:
                        cnt += 1
                        memo = information[0]-j
                        continue
                    else:
                        break
        else:
            if cnt > result:
                result = cnt

    print('#{} {}'.format(test_case, result))
