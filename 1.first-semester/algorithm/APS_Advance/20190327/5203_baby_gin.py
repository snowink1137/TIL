import sys

sys.stdin = open('5203.txt', 'r')


def baby_gin()


T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))

    A = []
    B = []
    for i in range(3):
        A.append(numbers[i*2])
        B.append(numbers[i*2+1])

    A.sort()
    if A[0] == A[1] == A[2]:
        print('#{} {}'.format(test_case, 1))
        continue
    elif A[0] + 1 == A[1] and A[1] + 1 == A[2]:
        print('#{} {}'.format(test_case, 1))
        continue

    if B[0] == B[1] == B[2]:
        print('#{} {}'.format(test_case, 2))
        continue
    elif B[0] + 1 == B[1] and B[1] + 1 == B[2]:
        print('#{} {}'.format(test_case, 2))
        continue

    flag = False
    for i in range(3, 6):
        A.append(numbers[i * 2])
        B.append(numbers[i * 2 + 1])

        A.sort()
        for j in range(i-1):
            temp = A[j:j+3]
            temp.sort()
            if temp[0] == temp[1] == temp[2]:
                print('#{} {}'.format(test_case, 1))
                flag = True
                break
            elif temp[0] + 1 == temp[1] and temp[1] + 1 == temp[2]:
                print('#{} {}'.format(test_case, 1))
                flag = True
                break

        if flag:
            break

        B.sort()
        for j in range(i - 1):
            temp = B[j:j + 3]
            temp.sort()
            if temp[0] == temp[1] == temp[2]:
                print('#{} {}'.format(test_case, 2))
                flag = True
                break
            elif temp[0] + 1 == temp[1] and temp[1] + 1 == temp[2]:
                print('#{} {}'.format(test_case, 2))
                flag = True
                break

        if flag:
            break

    if flag:
        continue
    else:
        print('#{} {}'.format(test_case, 0))
