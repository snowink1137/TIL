def solution(N, stages):
    challenger_num_list = [0 for _ in range(N+1)]
    fail_stage_check_list = [0 for _ in range(N+1)]
    for stage in stages:
        if stage > N:
            challenger_num_list[N] += 1
        else:
            fail_stage_check_list[stage] += 1

    for i in range(N, 0, -1):
        if i == N:
            challenger_num_list[i] += fail_stage_check_list[i]
        else:
            challenger_num_list[i] += challenger_num_list[i+1] + fail_stage_check_list[i]

    fail_ratio = [0 for _ in range(N+1)]
    for i in range(1, len(fail_ratio)):
        if challenger_num_list[i] == 0:
            fail_ratio[i] = 0
        else:
            fail_ratio[i] = fail_stage_check_list[i] / challenger_num_list[i]

    result = sorted(range(1, len(fail_ratio)), key=lambda x: fail_ratio[x], reverse=True)

    return result


stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5, stages))