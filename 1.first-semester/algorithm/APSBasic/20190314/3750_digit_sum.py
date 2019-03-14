import sys

sys.stdin = open('3750.txt', 'r')

T = int(input())
result_list = []
for test_case in range(1, T+1):
    n = int(input())

    while not 1 <= n <= 9:
        result = 0
        remain = n
        while True:
            if remain == 0 and n == 0:
                break

            remain = n % 10
            result += remain
            n = n // 10

        n = result

    result_list.append('#'+str(test_case))
    result_list.append(' '+str(n)+'\n')

print(''.join(result_list))
