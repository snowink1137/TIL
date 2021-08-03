import math

candidate = []


def permutation(depth, items, current, numbers):
    if depth == len(items):
        temp = int(''.join(map(lambda x: numbers[x], current)))
        if temp not in candidate:
            candidate.append(temp)
        return

    for i in items:
        if i in current:
            continue

        current_copy = current[:]
        current.append(i)
        if current:
            temp = int(''.join(map(lambda x: numbers[x], current)))
            if temp not in candidate:
                candidate.append(temp)

        permutation(depth+1, items, current, numbers)
        current = current_copy


def solution(numbers):
    answer = 0
    items = [int(n) for n in numbers]

    permutation(0, [i for i in range(len(items))], [], numbers)

    for c in candidate:
        if c < 2:
            continue

        for test_number in range(2, int(math.sqrt(c)+1)):
            if c % test_number == 0:
                break
        else:
            answer += 1

    return answer


numbers = '011'
print(solution(numbers))
