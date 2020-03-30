import sys

sys.stdin = open('1946.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    string = ''
    for i in range(N):
        C, K = input().split()
        string += C * int(K)

    print('#{}'.format(test_case))
    for i in range((len(string)//10)):
        print(string[(10*i):(10*(i+1))])

    print(string[10*(i+1):])
