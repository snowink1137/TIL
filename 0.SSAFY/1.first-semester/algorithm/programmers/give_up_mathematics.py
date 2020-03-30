def solution(answers):
    answer = []
    loof = [(1, 2, 3, 4, 5), (2, 1, 2, 3, 2, 4, 2, 5), (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)]
    score = 0

    for i in range(1, 4):
        temp = 0
        for j in range(len(answers)):
            if loof[i-1][j%len(loof[i-1])] == answers[j]:
                temp += 1

        if temp == score:
            score = temp
            answer.append(i)
        elif temp > score:
            score = temp
            answer = [i]

    answer.sort()
    return answer


answers = [1,2,3,4,5]
print(solution(answers))
