def solution(N, number):
    answer = -1
    answer_set_list = [0, {N}]

    for i in range(2, 9):
        mid_idx = i // 2
        answer_set = {int(str(N)*i)}

        for x_idx in range(1, mid_idx+1):
            for x in answer_set_list[x_idx]:
                for y in answer_set_list[i-x_idx]:
                    answer_set.add(x+y)
                    answer_set.add(x-y)
                    answer_set.add(x*y)
                    answer_set.add(x*(-y))

                    if x != 0:
                        answer_set.add(y//x)

                    if y != 0:
                        answer_set.add(x//y)

        if number in answer_set:
            return i

        answer_set_list.append(answer_set)

    return answer


N = 5
number = 12
print(solution(N, number))
