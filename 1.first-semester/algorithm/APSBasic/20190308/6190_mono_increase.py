import sys

sys.stdin = open('6190.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    monos = []
    length = len(numbers)
    for i in range(length):
        for j in range(i+1, length):
            number = numbers[i] * numbers[j]
            number = str(number)
            number_length = len(number)
            if number_length == 1:
                monos.append(int(number))
                continue

            for k in range(number_length - 1):
                if int(number[k])> int(number[k+1]):
                    break
            else:
                monos.append(int(number))

    result = -1
    if len(monos) != 0:
        result = max(monos)

    print('#{} {}'.format(test_case, result))
