def solution(k, room_number):
    answer = []
    visit = [0 for _ in range(k+1)]

    for number in room_number:
        if not visit[number]:
            answer.append(number)
            visit[number] += 1

            cnt3 = 1
            while number - cnt3 >= 0 and visit[number - cnt3]:
                visit[number - cnt3] += 1
                cnt3 += 1

            continue

        cnt = visit[number]
        while True:
            if not visit[number+cnt]:
                answer.append(number+cnt)
                visit[number+cnt] += 1

                cnt2 = 1
                while number - cnt2 >= 0 and visit[number - cnt2]:
                    visit[number - cnt2] += 1
                    cnt2 += 1

                break

            cnt += visit[number+cnt]

    return answer


k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))
