def solution(brown, red):
    answer = []
    total = brown + red

    for width_total in range(total-1, 0, -1):
        flag = False
        if total % width_total:
            continue

        height_total = total // width_total
        if height_total < 3:
            continue

        for width_red in range(red, 0, -1):
            if red % width_red:
                continue

            height_red = red // width_red

            if (width_total-2) * height_red == width_red * (height_total-2):
                answer.append(width_total)
                answer.append(height_total)

                flag = True
                break

        if flag:
            break

    return answer


brown = 24
red = 24
print(solution(brown, red))
