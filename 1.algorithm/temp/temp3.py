def solution(N, simulation_data):
    answer = 0
    counter = [0 for _ in range(N)]

    for data in simulation_data:
        min_index = 0
        min_value = 100000000
        for i in range(len(counter)):
            if counter[i] < min_value:
                min_value = counter[i]
                min_index = i

            if data[0] > counter[i]:
                counter[i] = data[0] + data[1]
                break
        else:
            diff = min_value - data[0]
            answer += diff
            counter[min_index] = diff + data[0] + data[1]

    return answer


N = 1
simulation_data = [[2, 3], [5, 4], [6, 3], [7, 4]]

print(solution(N, simulation_data))
