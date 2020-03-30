import math


def solution(s):
    answer = len(s)

    for i in range(1, int(len(s)/2)+1):
        temp_str = ''
        step = len(s) // i
        cnt = 1
        for j in range(0, step+1):
            if s[j*i:j*i+i] == s[j*i+i:j*i+2*i]:
                cnt += 1
            else:
                if cnt > 1:
                    temp_str = temp_str + str(cnt) + ''.join(s[j*i:j*i+i])
                    cnt = 1
                else:
                    temp_str = temp_str + ''.join(s[j*i:j*i+i])

        temp_length = len(temp_str)
        if temp_length < answer:
            answer = temp_length

    return answer


s = 'ababcdcdababcdcd'
print(solution(s))
