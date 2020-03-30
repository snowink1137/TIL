import sys

sys.stdin = open('1242.txt', 'r')

T = int(input())

check_idx = [-1, -2, -3, -4, -5, -6, -7]
code = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
for tc in range(1, T+1):
    N, M = map(int, input().split())

    list_set = set()
    pre = 0
    for _ in range(N):
        a = input().rstrip('0')
        if a == pre:
            pre = a
            continue

        pre = a

        binary_string = ''.join(map(lambda x: format(int(x, 16), '0>4b'), a))
        binary_string = binary_string.rstrip('0')

        cnt = 1
        while len(binary_string):
            temp = ''
            for idx in check_idx:
                temp = binary_string[idx*cnt] + temp

            if code.get(temp) is not None:
                original = binary_string[:]
                password = ''
                flag = False
                for i in range(8):
                    temp2 = ''
                    for idx in check_idx:
                        temp2 = binary_string[idx*cnt] + temp2

                    if code.get(temp2) is not None:
                        binary_string = binary_string[:(-7) * cnt]
                        password = str(code.get(temp2)) + password
                    else:
                        flag = True
                        break

                    if flag:
                        break

                if flag:
                    binary_string = original
                    cnt += 1
                    continue

                list_set.add(password)

                binary_string = binary_string.rstrip('0')
                cnt = 1
                continue
            else:
                cnt += 1

    result = 0
    for element in list_set:
        element = list(map(int, element))
        sum_temp = (element[0] + element[2] + element[4] + element[6]) * 3 + element[1] + element[3] + element[5] + element[7]
        if sum_temp % 10 == 0:
            result += sum(element)

    print('#{} {}'.format(tc, result))
