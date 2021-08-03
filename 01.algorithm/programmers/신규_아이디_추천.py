def solution(new_id):
    answer = []
    for char in new_id:
        answer.append(char.lower())

    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']

    check = []
    for i in range(len(answer)):
        if answer[i] not in char_list:
            check.append(i)

    check.reverse()
    for i in check:
        answer.pop(i)

    check = []
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            check.append(i+1)

    check.reverse()
    for i in check:
        answer.pop(i)

    if len(answer) != 0 and answer[0] == '.':
        answer.pop(0)

    if len(answer) != 0 and answer[-1] == '.':
        answer.pop()

    if len(answer) == 0:
        answer.append('a')

    if len(answer) >= 16:
        answer = answer[:15]

    if len(answer) != 0 and answer[-1] == '.':
        answer.pop()

    last_char = answer[-1]
    while len(answer) < 3:
        answer.append(last_char)

    answer = ''.join(answer)
    return answer


new_id = "z-+.^."
print(solution(new_id))
