def solution(number, k):
    answer = ''
    answer_list = []
    number_list = list(map(int, number))

    length = len(number_list)-k
    for i in range(len(number_list)):
        while answer_list and answer_list[-1] < number_list[i] and k > 0:
            answer_list.pop()
            k -= 1

        if k == 0:
            answer_list += list(number_list[i:])
            break

        answer_list.append(number_list[i])

    return ''.join(list(map(str, answer_list))[:length])


number = '4177252841'
k = 4
print(solution(number, k))
