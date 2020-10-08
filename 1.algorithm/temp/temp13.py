def big(s):
    answer = len(s) - 1
    while answer:
        cnt = len(s) - answer
        start = 0
        end = answer
        while cnt:
            if s[start] != s[end]:
                return answer

            start += 1
            end += 1
            cnt -= 1

        answer -= 1

    return answer


def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            answer += big(s[i:j+1])

    return answer


s = 'baby'
print(solution(s))
