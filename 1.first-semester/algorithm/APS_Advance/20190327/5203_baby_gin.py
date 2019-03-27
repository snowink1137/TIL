import sys

sys.stdin = open('5203.txt', 'r')


def baby_gin(arr):
    cnt_dict = dict()
    l = len(arr)
    for i in range(l):
        if cnt_dict.get(arr[i]):
            cnt_dict[arr[i]] += 1
        else:
            cnt_dict[arr[i]] = 1

    if 3 in cnt_dict.values():
        return True

    for i in range(l-2):
        cnt = 0
        if arr[i] + 1 in arr and arr[i] + 2 in arr:
            return True


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

    for i in range(3, 6):
        A.append(numbers[i * 2])
        B.append(numbers[i * 2 + 1])

        A.sort()
        a = baby_gin(A)
        if a:
            print('#{} {}'.format(test_case, 1))
            break

        B.sort()
        b = baby_gin(B)
        if b:
            print('#{} {}'.format(test_case, 2))
            break

    if a or b:
        continue
    else:
        print('#{} {}'.format(test_case, 0))
