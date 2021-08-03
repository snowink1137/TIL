def solution(name):
    answer = 0
    comback_move = 0
    name_ord_list = list(map(lambda x: abs(ord(x)-ord('A')) if abs(ord(x)-ord('A')) < 13 else 26-abs(ord(x)-ord('A')), name))
    zero_max_cnt = 0
    zero_last_idx = 0

    zero_cnt = 0
    for i, n in enumerate(name_ord_list):
        if not n:
            zero_cnt += 1
            if zero_cnt > zero_max_cnt:
                zero_max_cnt = zero_cnt
                zero_last_idx = i
        else:
            answer += n
            zero_cnt = 0

    zero_first_idx = zero_last_idx - zero_max_cnt + 1

    if zero_first_idx == 0 or zero_first_idx == len(name_ord_list) - 1:
        answer += (len(name_ord_list) - 1) - zero_max_cnt
    else:
        after_zero_last_idx_cnt = (len(name_ord_list) - 1) - zero_last_idx
        if zero_first_idx <= after_zero_last_idx_cnt:
            comeback_move = (zero_first_idx - 1) * 2 + after_zero_last_idx_cnt
        else:
            comeback_move = (zero_first_idx - 1) + after_zero_last_idx_cnt * 2

        answer += min(comeback_move, len(name_ord_list)-1)

    return answer


name = 'BBBBAAAAB'
print(solution(name))
