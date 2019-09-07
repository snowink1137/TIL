def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    enum_food_times = []
    for index, food_time in enumerate(food_times):
        enum_food_times.append([index, food_time])

    enum_food_times.sort(key=lambda x: x[1])
    length = len(enum_food_times)
    time = enum_food_times[0][1]
    cycle = 0
    cnt = 0

    while k > length * (time - cycle):
        k -= length * (time - cycle)
        length -= 1
        cycle += time - cycle
        # enum_food_times.pop(0)
        cnt += 1
        time = enum_food_times[cnt][1]

    enum_food_times = sorted(enum_food_times[cnt:], key=lambda x: x[0])
    answer = enum_food_times[k % length][0] + 1

    return answer


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
