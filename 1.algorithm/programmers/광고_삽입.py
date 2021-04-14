def solution(play_time, adv_time, logs):
    answer = ''

    play_time_timestamp = 0
    play_time_list = play_time.split(':')
    for i in range(3):
        play_time_timestamp += play_time_list[2-i] * (60 ** i)

    play_time_user_check = [0 for _ in range(play_time_timestamp)]

    for log in logs:
        temp_list = log.split('-')


    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))
