def solution(baseball):
    answer = 0
    for a in range(1, 10):
        for b in range(1, 10):
            if b == a:
                continue

            for c in range(1, 10):
                if c == b or c == a:
                    continue

                for i in range(len(baseball)):
                    strike = 0
                    ball = 0
                    numbers = list(map(int, str(baseball[i][0])))
                    if a == numbers[0]:
                        strike += 1
                    elif a in numbers:
                        ball += 1

                    if b == numbers[1]:
                        strike += 1
                    elif b in numbers:
                        ball += 1

                    if c == numbers[2]:
                        strike += 1
                    elif c in numbers:
                        ball += 1

                    if strike != baseball[i][1] or ball != baseball[i][2]:
                        break
                else:
                    answer += 1

    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))
