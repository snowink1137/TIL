def rank(hits_length):
    if hits_length >= 6:
        return 1
    elif hits_length == 0:
        return 6
    else:
        return 7-hits_length


def solution(lottos, win_nums):
    answer = []
    unknown_number_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            unknown_number_cnt += 1

    lottos_set = set(lottos)
    win_nums_set = set(win_nums)

    lower_hit = len(lottos_set.intersection(win_nums_set))
    higher_hit = lower_hit + unknown_number_cnt

    return [rank(higher_hit), rank(lower_hit)]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
