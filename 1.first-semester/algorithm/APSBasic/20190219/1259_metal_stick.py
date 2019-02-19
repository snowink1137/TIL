import sys

sys.stdin = open('1259_input.txt')


def check(current, remain):
    if not remain:
        return current

    new_remain = remain[:]
    new_current = current[:]
    for r in remain:
        if not new_current:
            new_current.append(r)
            new_remain.remove(r)
            return check(new_current, new_remain)
        else:
            if new_current[-1][-1] == r[0]:
                new_current.append(r)
                new_remain.remove(r)
                return check(new_current, new_remain)
            else:
                continue
    else:
        new_current.remove(current[0])
        new_remain.append(current[0])
        return check(new_current, new_remain)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    sticks = []
    dummy = list(map(int, input().split()))

    for i in range(N):
        sticks.append([dummy[2*i], dummy[2*i + 1]])

    result = check([], sticks)

    output = ''
    for element in result:
        output += ' '
        output += ' '.join(map(str, element))

    print(f'#{test_case} {output}')
