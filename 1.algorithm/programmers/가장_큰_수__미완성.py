def solution(numbers):
    temp_answer = []
    for number in numbers:
        number_str = str(number)
        temp_number_str = str(number)
        cnt = 0
        while len(temp_number_str) <= 4:
            temp_number_str += number_str[cnt]
            cnt = (cnt + 1) % len(number_str)

        temp_answer.append((temp_number_str, number_str))

    sorted_temp_answer = sorted(temp_answer, reverse=True)
    if sorted_temp_answer[0][1] == '0':
        return '0'

    answer = ''.join([number[1] for number in sorted_temp_answer])
    return answer


numbers = [21, 212]
print(solution(numbers))
