def solution(absolutes, signs):
    answer = 0

    for a, s in zip(absolutes, signs):
        sign = 1 if s else -1
        answer += a * sign

    return answer

