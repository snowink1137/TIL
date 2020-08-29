def solution(num, cards):
    answer = 0
    answer_list = [0 for _ in range(num+1)]

    for card in cards:
        if card > num:
            continue

        answer_list[card] = 1

    for i in range(1, num+1):
        if answer_list[i] == 0:
            continue

        for card in cards:
            if i + card > num:
                continue

            if answer_list[i+card] != 0 and answer_list[i] + 1 > answer_list[i+card]:
                continue

            answer_list[i+card] = answer_list[i] + 1

    if answer_list[-1] == 0:
        answer = -1
    else:
        answer = answer_list[-1]

    return answer


num = 8
cards = [1, 4, 6]
print(solution(num, cards))
