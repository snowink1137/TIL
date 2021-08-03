def solution(play_time, adv_time, logs):
    play_time_timestamp = get_timestamp(play_time)
    accumulated_user = [0 for _ in range(play_time_timestamp+1)]

    for log in logs:
        time_list = log.split('-')
        start = get_timestamp(time_list[0])
        end = get_timestamp(time_list[1])

        accumulated_user[start] += 1
        accumulated_user[end] -= 1

    for i in range(1, len(accumulated_user)):
        accumulated_user[i] = accumulated_user[i] + accumulated_user[i-1]

    for i in range(1, len(accumulated_user)):
        accumulated_user[i] = accumulated_user[i] + accumulated_user[i-1]

    adv_timestamp = get_timestamp(adv_time)

    max_user = accumulated_user[adv_timestamp]
    answer_timestamp = 0
    for i in range(adv_timestamp+1, play_time_timestamp+1):
        temp = accumulated_user[i] - accumulated_user[i-adv_timestamp]
        if temp > max_user:
            max_user = temp
            answer_timestamp = i - adv_timestamp + 1

    hour, answer_timestamp = divmod(answer_timestamp, 3600)
    answer = str(hour).zfill(2)

    minute, answer_timestamp = divmod(answer_timestamp, 60)
    answer += ':' + str(minute).zfill(2) + ':' + str(answer_timestamp).zfill(2)

    return answer


def get_timestamp(time):
    timestamp = 0
    play_time_list = time.split(':')
    for i in range(3):
        timestamp += int(play_time_list[2 - i]) * (60 ** i)
    return timestamp


play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))
