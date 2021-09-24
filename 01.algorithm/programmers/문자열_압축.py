def solution(s):
    answer = 1001

    cnt = 1
    while cnt <= len(s):
        candidate = []
        before = 0
        after = cnt
        while before < len(s):
            candidate.append(s[before:after])
            before += cnt
            after += cnt

        result = []
        multiple = 1
        memo = candidate.pop(0)
        while candidate:
            c = candidate.pop(0)
            if c == memo:
                multiple += 1
                continue
            else:
                if multiple == 1:
                    result.append(memo)
                else:
                    result.append(str(multiple) + memo)

                multiple = 1
                memo = c

        if multiple == 1:
            result.append(memo)
        else:
            result.append(str(multiple) + memo)

        a = len(''.join(result))
        if a < answer:
            answer = a

        cnt += 1

    return answer


s = "aabbaccc"
print(solution(s))
