def solution(s):
    answer = []
    parse = []

    s2 = s[2:-2]
    p1 = s2.split('},{')
    for p in p1:
        parse.append(set(p.split(',')))

    parse.sort(key=lambda x: len(x), reverse=True)

    if len(parse) == 1:
        answer.append(int(parse[0].pop()))
    else:
        for i in range(len(parse)-1):
            number = int((parse[i] - parse[i+1]).pop())
            answer.insert(0, number)
        else:
            answer.insert(0, int(parse[-1].pop()))

    return answer


s = "{{20,111},{111}}"
print(solution(s))
