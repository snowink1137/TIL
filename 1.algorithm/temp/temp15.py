def solution(k, score):
    diff_check = dict()
    score_check = [1 for _ in range(len(score))]
    # score_check[0] = 0

    for i in range(1, len(score)):
        diff = score[i-1] - score[i]
        if diff_check.get(diff):
            temp = diff_check.get(diff)
            if type(temp) == bool:
                score_check[i-1] = 0
                score_check[i] = 0
            else:
                temp.append(i)
                if len(temp) == k:
                    for j in temp:
                        score_check[j-1] = 0
                        score_check[j] = 0

                    diff_check[diff] = True
        else:
            diff_check[diff] = [i]

    return sum(score_check)


k = 3
score = [24,22,20,10,5,3,2,1]
print(solution(k, score))
