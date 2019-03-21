import sys

sys.stdin = open('4366.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    raw_number_2 = input()
    raw_number_3 = input()

    number_2 = int(raw_number_2, 2)
    number_3 = int(raw_number_3, 3)

    numbers_2 = []
    numbers_3 = []
    length_number_2 = len(raw_number_2)
    for i in range(length_number_2):
        if raw_number_2[length_number_2 - i - 1] == '0':
            numbers_2.append(number_2 + 1 * (2 ** i))
        else:
            numbers_2.append(number_2 - 1 * (2 ** i))

    length_number_3 = len(raw_number_3)
    for i in range(length_number_3):
        if raw_number_3[length_number_3 - i - 1] == '0':
            for j in range(1, 3):
                numbers_3.append(number_3 + j * (3 ** i))
        elif raw_number_3[length_number_3 - i - 1] == '1':
            temp = 0
            for j in range(0, 3, 2):
                numbers_3.append(number_3 + 1 * (3 ** i) * ((-1) ** temp))
                temp += 1
        else:
            temp = 1
            for j in range(0, 2):
                numbers_3.append(number_3 - temp * (3 ** i))
                temp += 1

    for number in numbers_2:
        if number in numbers_3:
            result = number
            break

    print('#{} {}'.format(tc, result))
